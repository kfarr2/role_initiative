from django import forms
from django.forms import ModelForm
from django.db import models
from django.forms import widgets
from django.contrib import auth
from django.contrib.auth.models import User
from .models import AccountModel


class AccountLoginForm(forms.ModelForm):
	username = forms.CharField(max_length=30)
	password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = AccountModel
		fields = (
			'username',
			'password',
		)
