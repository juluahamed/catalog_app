from django.shortcuts import render, redirect
from functools import wraps
from django.http import Http404
from authentication.views import showLogin
from wasp.models import Item, Category


def check_user_logged_in(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		if args[0].user.is_authenticated() == True:
			return func(*args, **kwargs)
		else:
			return redirect(showLogin)
	return wrapper

def check_item(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		print(kwargs['c_id'])
		if kwargs['c_id']:
			try:
				category = Category.objects.get(id=int(kwargs['c_id']))
			except Category.DoesNotExist:
				raise Http404("This category does not exsist")
			if kwargs['i_id']:
				try:
					item = Item.objects.get(id=int(kwargs['i_id']))
					try:
						int(kwargs['c_id'])
					except:
						raise Http404("Not a valid category id")
					if item.category.id == int(kwargs['c_id']):
						return func(item=item, *args, **kwargs)
					else:
						raise Http404("This Item does not exsist")	
				except Item.DoesNotExist:
					raise Http404("This Item does not exsist")
		raise Http404("This Item does not exsist")
	return wrapper