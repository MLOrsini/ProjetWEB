# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableaubord', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='heure',
            field=models.TimeField(auto_now=True),
        ),
    ]