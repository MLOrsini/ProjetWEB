from django.shortcuts import render
from tableaubord.models import Evenement,Utilisateur
from datetime import datetime
# Create your views here.
def tableaubord(request):
    exuser= Utilisateur(nom="tto",prenom="titi",sexe='F',tel="0645678953",mail="ttotiti@gmail.com")
    exuser.save()
    exemple=Evenement( nbPlaces=5 , description="C'est un exemple",createur=exuser, dateheure=datetime(2005,7,15,12,00))
    exemple.save()
    print(exemple.nbPlaces)
    evenements=Evenement.objects.all()
    return render(request,'tableaubord.html',{'evenements':evenements})
