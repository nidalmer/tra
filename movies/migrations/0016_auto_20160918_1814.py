# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-18 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_auto_20160918_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailer',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
