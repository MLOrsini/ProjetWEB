from django.core.management.base import BaseCommand
from django.shortcuts import render,redirect
from tableaubord.models import Evenement,Utilisateur, Sport,Participation
from datetime import datetime,timedelta
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class Command(BaseCommand):

	def handle(self, *args, **options):
		yesterday = datetime.now() - timedelta(days=1)
		events= Evenement.objects.filter(date__lte = yesterday)
		for event in events :
			print(event.description)
			participations=Participation.objects.all()
			for participation in participations:
				if (participation.evenement==event):
					participation.delete()
			event.delete()
		