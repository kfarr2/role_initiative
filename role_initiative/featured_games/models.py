import re
import os
from django.db import models
from django.conf import settings
from role_initiative.files.models import File


class GameInfoModel(File):
	"""
	All information regarding games
	"""
	game_id = models.AutoField(primary_key=True)
	game_type = models.CharField(max_length=250)	
