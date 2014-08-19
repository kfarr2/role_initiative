import random
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import DiceModel, RollButtonText
from .forms import DiceForm


def home(request):
	button_text = RollButtonText.objects.order_by('?')[0]	
	if request.method == 'GET':
		form = DiceForm(request.GET)
		if form.is_valid():
			total = rolling(form.cleaned_data['dice'], form.cleaned_data['sides'])
			return render(request, 'home/home.html',{
				'form' : form,
				'total': total,
				'button_text': button_text,
			})
	else:
		form = DiceForm()
	return render(request, 'home/home.html',{
		'form' : form,
		'button_text': button_text,
	})

def rolling(num_dice, num_sides):
	roll_total = 0 
	for x in range(0, num_dice):
		this_roll = random.randint(1, num_sides) 
		roll_total = roll_total + this_roll
	return roll_total

