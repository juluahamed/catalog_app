# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 05:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wasp', '0004_auto_20171102_1804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='image',
            new_name='document',
        ),
    ]