import random
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import Character, Games, DiceModel, RollButtonText
from .forms import DiceForm


def home(request):
	game_list = Games.objects.all()
	form = DiceForm(request.POST)
	button_text = RollButtonText.objects.order_by('?')[0]	
	
	return render(request, "home/home.html", {
		'game_list': game_list,
		'form': form,
		'button_text': button_text,
	})

def header(request):
	return render(request, "home/header.html")

def roll_dice(request):
	game_list = Games.objects.all()

	button_text = RollButtonText.objects.order_by('?')[0]	
	if request.method == 'GET':
		form = DiceForm(request.GET)
		if form.is_valid():
			total = rolling(form.cleaned_data['dice'], form.cleaned_data['sides'])
			return render(request, 'home/home.html',{
				'game_list': game_list,
				'form' : form,
				'total': total,
				'button_text': button_text,
			})
	else:
		form = DiceForm()
	return render(request, 'home/home.html',{
		'game_list': game_list,
		'form' : form,
		'button_text': button_text,
	})


def rolling(num_dice, num_sides):
	roll_total = 0 
	for x in range(0, num_dice):
		this_roll = random.randint(1, num_sides) 
		roll_total = roll_total + this_roll
	return roll_total

def character_sheet(request):
	character_sheet = Character.objects.all()
	return render(request, "home/charactersheet.html",{
		'character_sheet': character_sheet,
	})
