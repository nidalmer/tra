# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-29 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0018_movie_popularity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='tmdb_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]