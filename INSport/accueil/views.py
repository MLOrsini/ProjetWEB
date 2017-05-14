from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.shortcuts import render

# Create your views here.

def accueil(request):
    return render(request,'accueil.html')

def doc(request):
	return render(request,'aPropos.html')


