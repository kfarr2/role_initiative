import os, sys
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from models import GameInfoModel
from forms import GameForm

def game_view(request):
	"""
	View game
	"""
	games = GameInfoModel.objects.all()	

	return render(request, 'featured_games/game_list.html', {
		"games" : games,	
	})
		

def create(request):
	return _edit(request, game_id=None)

def edit(request, game_id):
	return _edit(request, game_id)

def _edit(request, game_id):
	if game_id == None:
		game = None 
	else:
		game = get_object_or_404(GameInfoModel, pk=game_id)

	if request.POST:
		form = GameForm(request.POST, instance=game) # this line is gonna be iffy
		if form.is_valid():
			game = form.save()
			return HttpResponseRedirect(reverse('featured_games-list'))
	else:
		form = GameForm(instance=game)

	return render(request, "featured_games/edit.html", {
		"chunk_size": settings.CHUNK_SIZE,
		"form": form,	
	})
	

	
