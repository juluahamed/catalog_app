# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout

# Create your views here.
def showLogin(request):
	"""View function returns the login page"""
	if request.user.is_authenticated() == True:
		return redirect(logout)
	else:
		return render(request, 'login.html', context=None)

def logout(request):
	auth_logout(request)
	return redirect(showLogin)

