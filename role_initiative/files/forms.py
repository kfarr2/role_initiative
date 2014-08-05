from django import forms
from models import File

class FileForm(forms.ModelForm):
	
	class Meta:
		model = File
		fields = (
			'name',
			'description',
		)
	
	def __init__(self, *args, **kwargs):
		super(FileForm, self).__init__(*args, **kwargs)

	def save(self, *args, **kwargs):
		user = kwargs.pop("user")
		to_return = super(FileForm, self).save(*args, **kwargs)
		return to_return
