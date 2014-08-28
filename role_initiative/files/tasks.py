from __future__ import absolute_import, print_function
import re
import collections
import tempfile
import sys
import os
import shutil
import subprocess
import datetime
import mimetypes
import hashlib

from celery import shared_task
from django.conf import settings
from django.db import IntegrityError, transaction, DatabaseError
from .enums import FileStatus, FileType, TEXT_FILE_MIME_TYPES

@shared_task
def process_uploaded_file(total_number_of_chunks, file):
	"""
	Recompiles uploaded chunks into a complete file,
	then converts the file to the correct file type if necessary.
	Updates the file model's path.
	"""

	try:
		os.makedirs(file.directory)
	except OSError as e:
		return False

	ext = os.path.splitext(file.name)[1] or ".unknown"
	final_file_path = os.path.join(file.directory, 'original' + ext)
	concatenated_file = open(final_file_path, "wb")

	# Combine all files into a file (chunk numbers start at 1)
	for i in range(1, total_number_of_chunks + 1):
		chunk_path = os.path.join(file.tmp_path, str(i) + '.part')
		shutil.copyfileobj(open(chunk_path, 'rb'), concatenated_file)

	shutil.rmtree(file.tmp_path)
	concatenated_file.close()
	file.file = os.path.relpath(final_file_path, settings.MEDIA_ROOT)
	file.status = FileStatus.FAILED
	mime_type = mimetypes.guess_type(final_file_path)[0]
	if mime_type in TEXT_FILE_MIME_TYPES:
		file.type = FileType.PDF
		
		# Possibly replace this with conditional code 
		file.status = FileStatus.READY
		
	# Make sure the file model still exists and only update the relevent fields
	with transaction.atomic():
		try:
			row = File.objects.select_for_update().get(pk=file.pk)
			file.save(update_fields=['file','type','status'])
		except(IndexError, DatabaseError, File.DoesNotExist) as e:
			return -1
		finally:
			shutil.rmtree(file.tmp_path)
	
	return file.status	
