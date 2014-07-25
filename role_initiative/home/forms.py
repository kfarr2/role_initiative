from django import forms
from django.forms import ModelForm
from models import DiceModel


class DiceForm(forms.ModelForm):

	class Meta:
		model = DiceModel
		fields = (
			'sides',
			'dice', 
		)
