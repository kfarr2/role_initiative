import os, sys
from django.conf import settings
from django.db import models
from role_initiative.files.models import File
from role_initiative.users.models import User

# Create your models here.
class Game(models.Model):
	"""
	Basic game model
	"""
	game_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	description = models.TextField()
	type = models.CharField(max_length=255)
	rulebook = models.ForeignKey(File)
	date_posted = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User)
	rating = models.IntegerField()

	class Meta:
		db_table = "games"
