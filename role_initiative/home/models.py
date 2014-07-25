import os
from django.db import models
from django.conf import settings


class DiceModel(models.Model):
	SIDES_CHOICES = (
		(4,'4'),
		(5,'5'),
		(6,'6'),
		(8,'8'),
		(10,'10'),
		(12,'12'),
		(14,'14'),
		(16,'16'),
		(20,'20'),
		(100,'100'),
	)

	sides = models.IntegerField(default=6, choices=SIDES_CHOICES)
	dice = models.IntegerField()

class RollButtonText(models.Model):
	button_text = models.CharField(primary_key=True, max_length=20)

class Games(models.Model):
	game_name = models.CharField(primary_key=True, max_length=50)

class Character(models.Model):
	'''
	Responsible for character database structure
	'''
	name = models.CharField(primary_key=True, max_length=50)
	char_class = models.CharField(max_length=50)
	char_skills = models.TextField()

	char_story = models.TextField()

	#Traits
	brawn = models.IntegerField(default=1)
	finesse = models.IntegerField(default=1)
	wits = models.IntegerField(default=1)
	resolve = models.IntegerField(default=1)
	panache = models.IntegerField(default=1)

	
