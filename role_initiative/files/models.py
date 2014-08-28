import re
import os
from django.db import models
from django.conf import settings
from role_initiative.users.models import User
from enums import FileType, FileStatus

class File(models.Model):
	file_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	description = models.TextField()
	file = models.FileField(upload_to=lambda *args, **kwargs: '')
	type = models.IntegerField(choices=FileType)
	status = models.IntegerField(choices=FileStatus)
	uploaded_on = models.DateTimeField(auto_now_add=True)
	edited_on = models.DateTimeField(auto_now=True)
	tmp_path = models.CharField(max_length=255, unique=True)

	uploaded_by = models.ForeignKey(User)

	class Meta:
		db_table = "file"
		ordering = ["-uploaded_on"]

	@classmethod
	def sanitize_filename(cls, filename):
		"""
		Only allow safe characters (no slashes). Any filename that is
		just a series of dots will be converted into the empty string
		"""
		filename = re.sub("[^A-Aa-z0-9._-]", "", filename)
		if filename.strip(".") == "":
			return ''
		return filename

	def size(self):
		if not hasattr(self, "_size"):
			self._size = get_size(self.directory)
		return self._size

	def directory(self):
		return os.path.join(settings.MEDIA_ROOT, str(self.pk))

	def path_with_extension(self, ext):
		return os.path.normpath(os.path.join(os.path.dirname(self.file.path), "file."+ ext))
	
	def url_with_extension(self, ext):
		return os.path.normpath(settings.MEDIA_URL + os.path.relpath(os.path.dirname(self.file.path), settings.MEDIA_ROOT) + "/file." + ext)
	

	def __unicode__(self):
		return "%s (%s)" % (self.name, FileType._choices[self.type][1])


