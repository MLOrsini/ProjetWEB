from .forms import UserForm, AdherenceForm, SportForm
from tableaubord.models import Utilisateur, Sport, Adherence, Participation,Evenement
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required



# Page My Profile, où on peut modifier son profil -------------------
@login_required
def Utilisateurs(request):
	utilisateur=request.user.profile
	sports=Sport.objects.all()

	form = UserForm(request.POST,request.FILES, instance=utilisateur)
	# Ne marche pas si on ne met pas instance = utilisateur car le champ id serait vide vu qu'on exclu user du formulaire!
	if form.is_valid():
		form.save()
	else:
		form=UserForm(instance=utilisateur)
		form.merge_from_initial()
		list_exp= sports
		sports = request.POST.getlist('choix')
		if(request.POST.get('choix')):
			print("reter")
			Adherence.objects.filter(adherent_id=request.user.id).delete()
			for sport in sports:
					ad=Adherence(adherent=request.user,sport=Sport.objects.get(pk=sport))
					ad.save()

		form3 = SportForm(request.POST)
		if form3.is_valid():
			form3.save()
	return render(request, 'Utilisateur.html', locals())



@login_required
#Page profil, inutile?? -------------------------------------------
def profil(request):
	return render(request, 'profil.html')




# Afficher un profil d'utilisateur --------------------------------
@login_required
def monProfil(request,id):
	if request.user.is_authenticated():
		utilisateur=Utilisateur.objects.get(pk=id)
		user=User.objects.get(pk=id)
		sports=Sport.objects.all()
		adherences=Adherence.objects.all()
		return render(request, 'monProfil.html',locals())
	return redirect('/login')



# Supprimer son profil ----------------------------------------------
@login_required
def deleteUser(request):
	if request.user.is_authenticated():
		use=request.user
		id = request.user.id
		try:
			ads=Adherence.objects.get(adherent_id=use.id)
			for ad in ads:
				ad.delete()
		except:
			ads = None;

		try:
			parts= Participation.objects.get(participant_id=use.id)
			for part in parts:
				part.delete()
		except :
			parts=None;

		try:

			events= Evenement.objects.get(createur_id=use.id)
			for event in events:
				event.delete()
		except:
			events = None

		auth.logout(request)

		U=Utilisateur.objects.get(pk=id)
		U.delete()
		use.delete()

		return redirect('/')
	return redirect('/')
