from django import forms
from django.forms import ModelForm
from models import GameInfoModel

class GameForm(forms.ModelForm):

	class Meta:
		model = GameInfoModel
		fields = (
			'name',
			'game_type',
			'description',
			'file',
		)


