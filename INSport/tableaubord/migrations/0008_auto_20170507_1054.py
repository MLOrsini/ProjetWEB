# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 10:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableaubord', '0007_auto_20170507_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='photoProfil',
            field=models.ImageField(default='photosProfil/profil.jpeg', upload_to='photosProfil/'),
        ),
        migrations.AlterField(
            model_name='evenement',
            name='dateheure',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 7, 10, 54, 43, 556291), verbose_name='Date/heure evenement '),
        ),
    ]
