import random
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from role_initiative.games.models import Game
from .models import DiceModel, RollButtonText
from .forms import DiceForm


def home(request):
	button_text = RollButtonText.objects.order_by('?')[0]	
	games = Game.objects.all()
	if request.method == 'GET':
		form = DiceForm(request.GET)
		if form.is_valid():
			rolled = rolling(form.cleaned_data['dice'], form.cleaned_data['sides'])
			rolled.sort()
			total = 0
			for x in range(len(rolled)):
				total += rolled[x]

			return render(request, 'home/home.html',{
				'form' : form,
				'games': games,
				'rolled': rolled,
				'total': total,
				'button_text': button_text,
			})
	else:
		form = DiceForm()


	return render(request, 'home/home.html',{
		'games': games,
		'form' : form,
		'button_text': button_text,
	})

def rolling(num_dice, num_sides):
	rolled = [None]*num_dice
	for x in range(0, num_dice):
		this_roll = random.randint(1, num_sides) 
		rolled[x] = this_roll
	return rolled

