import os, sys
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from models import Game

def list_(request):
	"""
	List all games
	"""
	games = Game.objects.all()

	return render(request, 'games/list.html', {
		"games": games,	
	})
