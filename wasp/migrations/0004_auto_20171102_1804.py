# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wasp', '0003_category_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='item_image/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='wasp.User'),
            preserve_default=False,
        ),
    ]
