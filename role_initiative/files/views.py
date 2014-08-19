import os, sys, shutil, math
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.db import transaction, DatabaseError
from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from models import File
from forms import FileForm

#def list_(request):

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
			# type= ...get the enums together and fix this shit
			# status=
			uploaded_by=request.user.id,
			tmp_path=dir_path,
		)
		f.save()
	except DatabaseError as e:
		# that file was already taken care of, dude
		return HttpResponse("OK")

	#process_uploaded_file.delay(total_number_of_chunks, f)
	return HttpResponse("COMPLETE")
