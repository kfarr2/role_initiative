from django import forms
from django.db import models

class AccountModel(models.Model):
	username = models.CharField(primary_key=True, max_length=30)
	password = models.CharField(max_length=40)

	
