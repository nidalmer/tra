# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-07 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20160907_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imdb_id',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
