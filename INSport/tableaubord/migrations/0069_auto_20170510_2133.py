# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 21:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableaubord', '0068_auto_20170510_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='dateheure',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 10, 21, 33, 24, 260402), verbose_name='Date/heure evenement '),
        ),
    ]
