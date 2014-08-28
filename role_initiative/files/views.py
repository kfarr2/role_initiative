import os, sys, shutil, math
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.db import transaction, DatabaseError
from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib import messages
from models import File
from enums import FileType, FileStatus
from forms import FileForm
from tasks import process_uploaded_file

def list_(request):
	"""
	List files.
	-add a search form

	"""
	files = File.objects.all()
	
	uploaded = File.objects.filter(
		status=FileStatus.UPLOADED,
		uploaded_by=request.user,
	)
	
	failed = File.objects.filter(
		status=FileStatus.FAILED,
		uploaded_by=request.user,
	)

	return render(request, 'files/list.html', {
		"files": files,
		"uploaded": uploaded,
		"failed": failed,
	})

def detail(request, file_id):
	"""
	Detail view of a file.
	"""
	
	_file = get_object_or_404(File, pk=file_id)

	return render(request, 'files/detail.html', {
		"file": _file,
	})

def edit(request, file_id):
	"""
	Edit a file
	"""

	_file = get_object_or_404(File, pk=file_id)

	return render(request, 'files/edit.html', {
		"file": _file,	
	})

def upload(request):
	"""
	Generates the upload view.
	"""
	if request.method == "POST":
		if request.POST.get("error_message"):
			messages.error(request, request.POST["error_message"])
			return HttpResponse(request.POST["error_message"])
		else:
			messages.success(request, "Files Uploaded!")
		return HttpResponseRedirect(reverse("files-upload"))
	
	return render(request, "files/upload.html", {
		"chunk_size": settings.CHUNK_SIZE,
	})

def delete(request, file_id):
	"""
	Deletes a file.
	"""
	_file = get_object_of_404(File, pk=file_id)

	if request.method == "POST":
		_file.delete()
		return HttpResponseRedirect(reverse('files-list'))

	return render(request, "files/delete.html", {
		"file": _file,
	})

def media(request, path):
	"""
	Returns a response containing the contents of the file.
	"""
	path = os.path.join(settings.MEDIA_ROOT, path)
	file = open(path, "r")
	file.seek(0, os.SEEK_END)
	length = file.tell()
	file.seek(0)

	return HttpResponse(file)

@csrf_exempt
def store(request):
	"""
	This view recieves a chunck of a file and saves it. When all the chunks are
	uploaded, they are joined together to make a complete file.

	This is gonna be pretty sketch for a while
	"""
	guid = File.sanitize_filename(request.POST['resumableIdentifier'])
	if not guid:
		return HttpResponseNotFound("Invalid file identifier")

	dir_path = os.path.join(settings.TMP_ROOT, str(request.user.pk) + "-" + guid)
	try:
		os.makedirs(dir_path)
	except OSError as e:
		# directory exists, dude!
		pass

	# each file will be named 1.part, 2.part etc. and stored inside the dir_path
	file_path = os.path.join(dir_path, str(int(request.POST['resumableChunkNumber'])) + '.part')
	file = request.FILES['file']

	# dont let that chunk be too big
	if file.size > (settings.CHUNK_SIZE*2):
		shutil.rmtree(dir_path)
		return HttpResponseNotFound("Too many chunks")

	with open(file_path, 'wb') as dest:
		for chunk in file.chunks():
			dest.write(chunk)

	total_number_of_chunks = int(request.POST['resumableTotalChunks'])
	total_number_of_uploaded_chunks = len(os.listdir(dir_path))
	if total_number_of_chunks != total_number_of_uploaded_chunks:
		return HttpResponse("OK")

	total_size = 0
	for i in range(1, total_number_of_chunks + 1):
		chunk_path = os.path.join(dir_path, str(i) + '.part')
		total_size += os.path.getsize(chunk_path)
		if total_size > settings.MAX_UPLOAD_SIZE:
			shutil.rmtree(dir_path)
			return HttpResponseNotFound("File too big")

	if total_size != int(request.POST['resumableTotalSize']):
		# All files present and accounted for, 
		# just slow as balls when it comes to getting written
		return HttpResponse("OK")

	try:
		f = File(
			name=request.POST['resumableFilename'],
			type=FileType.UNKNOWN,
			status=FileStatus.UPLOADED,
			uploaded_by=request.user,
			tmp_path=dir_path,
		)
		f.save()
	except DatabaseError as e:
		# that file was already taken care of, dude
		return HttpResponse("OK")

	process_uploaded_file.delay(total_number_of_chunks, f)
	return HttpResponse("COMPLETE")
