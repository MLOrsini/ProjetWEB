from .forms import UserForm, AdherenceForm, SportForm
from tableaubord.models import Utilisateur, Sport
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def Utilisateur(request):
	utilisateur=request.user.profile
	sports=Sport.objects.all()

	form = UserForm(request.POST,request.FILES)  
	if form.is_valid():
		form.save() 

	form2 = AdherenceForm(request.POST, instance=utilisateur)  
	if form2.is_valid():
		form2.save()  

	form3 = SportForm(request.POST)  
	if form3.is_valid():
		form3.save()  


	return render(request, 'Utilisateur.html', locals())




def profil(request):
	return render(request, 'profil.html')


#@login_required
def monProfil(request):
	if request.user.is_authenticated():
		return render(request, 'monProfil.html')
	return redirect('/login')


