import re
import os
from django.db import models
from django.conf import settings
from role_initiative.files.models import File


class GameInfoModel(models.Model):
	"""
	All information regarding games
	"""
	game_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=250)
	game_type = models.CharField(max_length=250)	
	description = models.TextField()
	file = models.ForeignKey(File, null=True, on_delete=models.SET_NULL)
