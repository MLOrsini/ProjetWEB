# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 22:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableaubord', '0029_auto_20170507_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='dateheure',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 7, 22, 34, 57, 19483), verbose_name='Date/heure evenement '),
        ),
    ]