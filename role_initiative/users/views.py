import os
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.contrib.auth import login as django_login, logout as django_logout, get_user_model
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.http import is_safe_url
from role_initiative.games.models import Game
from forms import LoginForm, UserForm
from models import User

# Create your views here.
def games(request):
	"""
	Default game view
	"""
	pass

def home(request, user_id):
	"""

	"""
	user = User.objects.get(user_id=user_id)
	games = Game.objects.filter(created_by=request.user)

	return render(request, 'users/home.html', {
		"user": user,
		"games": games,
	})

def login(request):
	"""
	Default login view
	"""
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse("home"))

	if request.POST:
		form = LoginForm(request.POST)
		if form.is_valid():
			django_login(request, form.cleaned_data['user'])
			safe_url = reverse("home")
			url = form.cleaned_data.get("next", safe_url)
			if is_safe_url(url, host=request.get_host()):
				return HttpResponseRedirect(url)

			return HttpResponseRedirect(safe_url)
	else:
		form = LoginForm(initial=request.GET)
	
	return render(request, 'users/login.html', {
		'form': form,	
	})

def create(request):
	return _edit(request, user_id=None)

def edit(request, user_id):
	return _edit(request, user_id)

def _edit(request, user_id):
	"""
	Default user create view
	"""
	if user_id is None:
		user = None
	else:
		user = get_object_or_404(User, pk=user_id)

	if request.POST:
		form = UserForm(request.POST, instance=user, user=request.user)
		if form.is_valid():
			user = form.save()
			return HttpResponseRedirect(reverse("home"))

	else:
		form = UserForm(instance=user, user=request.user)

	return render(request, 'users/login.html', {
		'form': form,			
	})


