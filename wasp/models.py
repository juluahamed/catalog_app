# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=120, unique=True)
	time_created = models.DateTimeField(editable=False)
	time_updated = models.DateTimeField()
	
	def __unicode__(self): # For Python 2, use __unicode__ too
		return self.name
	
	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
		    self.time_created = timezone.now()
		self.time_updated = timezone.now()
		return super(User, self).save(*args, **kwargs)


class Category(models.Model):
	name = models.CharField(max_length=50)
	user_id = models.ForeignKey(User)
	document = models.ImageField(upload_to='category_image/')
	time_created = models.DateTimeField(editable=False)
	time_updated = models.DateTimeField()
	
	def __unicode__(self): # For Python 2, use __unicode__ too
		return self.name
	
	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
		    self.time_created = timezone.now()
		self.time_updated = timezone.now()
		return super(Category, self).save(*args, **kwargs)

class Item(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(max_length=300, default='')
	user_id = models.ForeignKey(User)
	category = models.ForeignKey(Category)
	document = models.ImageField(upload_to='item_image/')
	time_created = models.DateTimeField(editable=False)
	time_updated = models.DateTimeField()
	
	def __unicode__(self): # For Python 2, use __unicode__ too
		return self.name
	
	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
		    self.time_created = timezone.now()
		self.time_updated = timezone.now()
		return super(Item, self).save(*args, **kwargs)
