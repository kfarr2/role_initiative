from django.shortcuts import render
from django.views.generic import View
from .forms import AccountLoginForm

def login(request):
	form = AccountLoginForm(request.POST)

	return render(request, "login/login_screen.html", {
		'form': form,
	})


