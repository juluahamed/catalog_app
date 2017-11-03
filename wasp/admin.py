# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from wasp.models import User, Category, Item

# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Item)
