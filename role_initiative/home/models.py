import os
from django.db import models
from django.conf import settings


class DiceModel(models.Model):
	SIDES_CHOICES = (
		(4,'4'),
		(6,'6'),
		(8,'8'),
		(10,'10'),
		(12,'12'),
		(20,'20'),
		(100,'100'),
	)

	sides = models.IntegerField(default=6, choices=SIDES_CHOICES)
	dice = models.IntegerField()

class RollButtonText(models.Model):
	button_text = models.CharField(primary_key=True, max_length=20)
