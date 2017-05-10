# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 20:42
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tableaubord', '0067_auto_20170510_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participe', models.CharField(choices=[('-1', 'pas croise'), ('0', 'Oui'), ('1', 'Non')], default='-1', max_length=8)),
            ],
        ),
        migrations.AlterField(
            model_name='evenement',
            name='dateheure',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 10, 20, 42, 34, 509985), verbose_name='Date/heure evenement '),
        ),
        migrations.AddField(
            model_name='participation',
            name='evenement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tableaubord.Evenement'),
        ),
        migrations.AddField(
            model_name='participation',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
