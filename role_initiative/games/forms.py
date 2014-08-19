import os, sys
from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from models import Game

class GameForm(forms.ModelForm):
	"""

	"""

	class Meta:
		model = Game
		fields = (
			'name',
			'description',
			'type',
			'rulebook',
		)

	def __init__(self, *args, **kwargs):
		super(GameForm, self).__init__(*args, **kwargs)

	def save(self, *args, **kwargs):
		user = kwargs.pop("user")
		to_return = super(GameForm, self),save(*args, **kwargs)
		
		
		return to_return
