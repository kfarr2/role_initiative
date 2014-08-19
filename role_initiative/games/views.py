import os, sys
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from models import Game
from forms import GameForm

def list_(request):
	"""
	List all games
	"""
	games = Game.objects.all()

	return render(request, 'games/list.html', {
		"games": games,	
	})

def create(request):
	return _edit(request, game_id=None)

def _edit(request, game_id):
	"""
	Edit or create a game
	"""
	if game_id == None:
		game = None
	else:
		game = get_object_or_404(Game, pk=game_id)

	if request.method == "POST":
		form = GameForm(irequest.POST, instance=game)
		if form.is_valid():
			form.save(user=request.user)
			return HttpResponseRedirect(reverse("games-detail", args=(file.pk,)))
	else:
		form = GameForm(instance=game)

	return render(request, 'games/edit.html', {
		"game": game,	
		"form": form,	
	})
