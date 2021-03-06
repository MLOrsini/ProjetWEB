from django.shortcuts import render,redirect
from tableaubord.models import Evenement,Utilisateur, Sport,Participation
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import UtilisateurForm,UserForm, createEventForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
#page d'exemple pour afficher des événements --------------



#Création compte : ---------------------------------------
def sign1(request):
	form = UserForm(request.POST or None)
	evenements=Evenement.objects.all()
	if form.is_valid() :
		new_user = User.objects.create_user(**form.cleaned_data)
		username = form.cleaned_data["username"]
		password = form.cleaned_data["password"]
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)  # nous connectons l'utilisateur
			for e in evenements : #On initialise participations à -1 pour tous les events pour qu'ils soient proposés dans le swipe
				p=Participation(participant=user,evenement=e,participe='-1')
				p.save()
			return redirect('Utilisateur')

	return render(request, 'sign1.html',locals())

@login_required
def tableaubord(request):
	evenements=Evenement.objects.all()
	return render(request,'tableaubord.html',{'evenements':evenements})



#Création evenement : ---------------------------------------
@login_required
def createEvent(request):
	user=request.user
	ev=Evenement.objects.all()
	form=createEventForm(request.POST or None,request.FILES)
	if form.is_valid():
		ev=form.save(commit=False)
		ev.createur=user
		ev.placesRestantes=ev.nbPlaces
		ev.save()
		users=User.objects.all()
		for u in users:
			p=Participation(participant=u,evenement=ev,participe='-1')
			p.save()
		return redirect('/tableaubord')
	return render(request, 'createEvent.html',locals())


# Suppression evenement : -------------------------------------
@login_required
def deleteEvent(request,id):
	event = Evenement.objects.get(pk=id)
	participations=Participation.objects.all()
	for participation in participations:
		if (participation.evenement==event):
			participation.delete()
	event.delete()
	ev=Evenement.objects.all()
	return render(request,'tableaubord.html',{'evenements':ev})
