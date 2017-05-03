from django.shortcuts import render
from tableaubord.models import Evenement,Utilisateur

# Create your views here.
def tableaubord(request):
    exuser= Utilisateur(id=1,nom="tto",prenom="titi",sexe='F',tel="0645678953",mail="ttotiti@gmail.com")
    exuser.save()
    exemple=Evenement(id=1, nbPlaces=5 , description="C'est un exemple",createur=exuser)
    exemple.save()
    print(exemple.nbPlaces)
    evenements=Evenement.objects.all()
    return render(request,'tableaubord.html',{'evenements':evenements})
