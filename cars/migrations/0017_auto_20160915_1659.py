# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-15 11:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0016_auto_20160915_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testdrive',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 15, 16, 59, 39, 627994)),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 15, 16, 59, 39, 626993)),
        ),
    ]
