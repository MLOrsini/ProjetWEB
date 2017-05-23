# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 14:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableaubord', '0091_auto_20170513_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 13, 14, 48, 36, 61278), verbose_name='Date événement'),
        ),
        migrations.AlterField(
            model_name='evenement',
            name='heure',
            field=models.CharField(default='Heure indéfinie', max_length=20),
        ),
        migrations.AlterField(
            model_name='evenement',
            name='nbPlaces',
            field=models.IntegerField(verbose_name='Nombre de places'),
        ),
        migrations.AlterField(
            model_name='evenement',
            name='photoEvt',
            field=models.ImageField(default='photoEvt/evtbase.png', upload_to='photoEvt/', verbose_name="Photo de l'événement"),
        ),
        migrations.AlterField(
            model_name='evenement',
            name='placesRestantes',
            field=models.IntegerField(default=0, verbose_name='Nombre de places restantes'),
        ),
    ]