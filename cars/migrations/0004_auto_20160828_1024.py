# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-28 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20160828_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.FloatField(),
        ),
    ]
