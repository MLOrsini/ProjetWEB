# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 09:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableaubord', '0088_auto_20170513_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 13, 9, 42, 21, 158399), verbose_name='Date evenement'),
        ),
    ]