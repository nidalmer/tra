# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-16 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0013_movie_backdrop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='tmdb_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]