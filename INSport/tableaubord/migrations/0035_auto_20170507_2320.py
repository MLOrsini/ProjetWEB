# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 23:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableaubord', '0034_auto_20170507_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='dateheure',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 7, 23, 20, 52, 422905), verbose_name='Date/heure evenement '),
        ),
    ]
