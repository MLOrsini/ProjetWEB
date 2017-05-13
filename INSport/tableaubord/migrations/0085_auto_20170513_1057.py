# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 10:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableaubord', '0084_auto_20170512_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evenement',
            name='dateheure',
        ),
        migrations.AddField(
            model_name='evenement',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 13, 10, 57, 27, 251903), verbose_name='Date evenement'),
        ),
        migrations.AddField(
            model_name='evenement',
            name='heure',
            field=models.CharField(default='Pas heure', max_length=20),
        ),
        migrations.AddField(
            model_name='evenement',
            name='placesRestantes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evenement',
            name='titre',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='evenement',
            name='description',
            field=models.TextField(),
        ),
    ]
