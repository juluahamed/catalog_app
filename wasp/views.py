# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, Http404
from authentication.utils import check_user_logged_in, check_item
from .forms import CategoryForm, ItemForm
from wasp.models import User, Category, Item
import random
import string

def index(request):
	request.session['fav_color'] = 'blue'
	context_dict={'hello':request.session['fav_color']}
	return render(request, 'base.html', context= context_dict)

def category(request):
	if request.user.is_authenticated:
		email = request.user.email
		username= request.user.username
		if len(User.objects.filter(email=request.user.email)) == 0:
			user = User.objects.create(name=request.user.username, email=request.user.email)
			user.save()
	categories = Category.objects.all()

	return render(request, 'category.html', {'categories': categories})

@check_user_logged_in
def newCategory(request):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = CategoryForm(request.POST,request.FILES)
		# check whether it's valid:
		if form.is_valid():
			instance = Category(name=form.cleaned_data['name'], document=form.cleaned_data['document'], user_id= User.objects.get(email=request.user.email))
			instance.save()
			return redirect(category)
		else:
			return redirect(category)

		# if a GET (or any other method) we'll create a blank form
	else:
		form = CategoryForm()
		return render(request, 'newCategory.html', {'form': form})

def viewCategory(request, id=None):
	if id:
		try:
			category = Category.objects.get(id=id)
		except Category.DoesNotExist:
			raise Http404("This category does not exsist")
		items = Item.objects.filter(category= category.id)

	return render(request, 'viewCategory.html', {'items': items})

@check_user_logged_in
def newItem(request):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ItemForm(request.POST,request.FILES)
		# check whether it's valid:
		if form.is_valid():
			instance = Item(name=form.cleaned_data['name'], description= form.cleaned_data['description'],
							document= form.cleaned_data['document'],
							 user_id= User.objects.get(email=request.user.email),
							 category= form.cleaned_data['category'])
			instance.save()
			return redirect(viewCategory, id =form.cleaned_data['category'].id)
		else:
			return redirect(viewCategory, id =form.cleaned_data['category'].id)
	else:
		form = ItemForm()
		return render(request, 'newItem.html', {'form': form})

@check_item
def viewItem(request, c_id=None, i_id=None, item=None):
	return render(request, 'viewItem.html', {'item': item})

@check_user_logged_in
@check_item	
def editItem(request, c_id=None, i_id=None, item=None):
	if request.method == 'POST':
		if len(request.FILES) == 0:
			request.FILES['document'] = item.document
		# create a form instance and populate it with data from the request:
		form = ItemForm(request.POST,request.FILES)
		# check whether it's valid:
		if form.is_valid():
			instance = Item.objects.get(id=i_id)
			instance.name= form.cleaned_data['name']
			instance.description= form.cleaned_data['description']
			instance.document = form.cleaned_data['document']
			instance.user_id= User.objects.get(email=request.user.email)
			instance.category= form.cleaned_data['category']
			instance.save()
			return redirect(viewCategory, id =form.cleaned_data['category'].id)
		else:
			return redirect(viewCategory, id =form.cleaned_data['category'].id)
	else:
		form = ItemForm(initial={'id': item.id, 'name': item.name, 'description': item.description,
						 'document': item.document, 'category': item.category})
		return render(request, 'editItem.html', {'form': form})

@check_user_logged_in
@check_item
def deleteItem(request, c_id=None, i_id=None, item=None):
	if request.method == 'POST':
		instance = Item.objects.get(id= i_id)
		instance.delete()
		return redirect(viewCategory, id= c_id)
	return render(request, 'deleteItem.html', {'item': item})






