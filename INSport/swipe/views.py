from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from tableaubord.models import Evenement,Utilisateur,Sport,Adherence,Participation
from . import models


@login_required
def index(request):
    try:
        context=Evenement.objects.raw('SELECT tableaubord_evenement.id,tableaubord_evenement.description FROM tableaubord_evenement INNER JOIN tableaubord_participation ON tableaubord_evenement.id = tableaubord_participation.evenement_id WHERE tableaubord_participation.participant_id=1 AND tableaubord_participation.participe=-1;' )[0]
    except IndexError:
        context= None
    return render(request, 'index.html',{'context': context})


def create_vote(request, event_id, vote):
    event = Evenement.objects.get(pk=event_id)
    part=Participation.objects.filter(evenement=event, participant= request.user)

    
    if vote:
        part.update(participe='0')
    else :
        part.update(participe='1')
    return redirect('index')


@login_required
def nice(request, event_id):
    return create_vote(request, event_id, True)


@login_required
def nope(request, event_id):
    return create_vote(request, event_id, False)


