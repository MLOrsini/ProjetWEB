from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from tableaubord.models import Evenement,Utilisateur,Sport,Adherence,Participation
from . import models

#from django.http import HttpResponse
# Create your views here.

@login_required
def evenement(request):

	try:
		context=Evenement.objects.raw('SELECT tableaubord_evenement.id,tableaubord_evenement.description FROM tableaubord_evenement INNER JOIN tableaubord_participation ON tableaubord_evenement.id = tableaubord_participation.evenement_id WHERE tableaubord_participation.participant_id=%s AND tableaubord_participation.participe=0;',(request.user.id,))
	except :
		context= None
	
	return render(request, 'evenement.html',{'context': context})

@login_required
def detailevenement(request,id):
	participations=Participation.objects.all()
	detail=Evenement.objects.get(pk=id)
	user=User.objects.all()
	
	createurEvt=detail.createur_id
	createurInfo=Utilisateur.objects.get(pk=createurEvt)

	photoEvt=detail.sports_id
	photoSport=Sport.objects.get(pk=photoEvt)
	return render(request,'detailEvenement.html',locals())

@login_required
def dislikeEvent(request,id):
	event = Evenement.objects.get(pk=id)
	part=Participation.objects.filter(evenement=event, participant= request.user)
	part.update(participe='1')
	try:
		context=Evenement.objects.raw('SELECT tableaubord_evenement.id,tableaubord_evenement.description FROM tableaubord_evenement INNER JOIN tableaubord_participation ON tableaubord_evenement.id = tableaubord_participation.evenement_id WHERE tableaubord_participation.participant_id=%s AND tableaubord_participation.participe=0;',(request.user.id,))
	except :
		context= None
	
	return render(request, 'evenement.html',{'context': context})


