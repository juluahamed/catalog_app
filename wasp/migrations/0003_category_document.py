# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 12:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wasp', '0002_auto_20171031_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='document',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='category_image/'),
            preserve_default=False,
        ),
    ]
