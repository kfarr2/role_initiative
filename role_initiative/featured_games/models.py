import os
from django.db import models
from django.conf import settings

class GameInfoModel(models.Model):
	"""
	All information regarding games
	"""
	game_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=250)
	game_type = models.CharField(max_length=250)	
	description = models.TextField()	




