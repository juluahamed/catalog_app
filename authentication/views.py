# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout

# Create your views here.
def showLogin(request):
	"""View function returns the login page. Creates anti-forgery state token"""
	# state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
	# #session['state'] = state
	if request.user.is_authenticated() == True:
		return redirect(logout)
	else:
		return render(request, 'login.html', context=None)

def logout(request):
	print(request.user)
	auth_logout(request)
	print(request.user)
	return redirect(showLogin)

