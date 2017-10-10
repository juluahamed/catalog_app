# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=120, unique=True)
	picture = models.CharField(max_length=250)
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