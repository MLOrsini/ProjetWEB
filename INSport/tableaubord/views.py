from django.shortcuts import render
from tableaubord.models import Evenement,Utilisateur
from datetime import datetime
from .forms import UtilisateurForm

# Create your views here.
def tableaubord(request):
	exuser= Utilisateur(nom="tto",prenom="titi",sexe='F',tel="0645678953",mail="ttotiti@gmail.com")
	exuser.save()
	exemple=Evenement( nbPlaces=5 , description="C'est un exemple",createur=exuser, dateheure=datetime(2005,7,15,12,00))
	exemple.save()
	print(exemple.nbPlaces)
	evenements=Evenement.objects.all()
	return render(request,'tableaubord.html',{'evenements':evenements})


def utils(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
	form = UtilisateurForm(request.POST or None,request.FILES)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
	if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
		form.save()
		nom = form.cleaned_data['nom']
		prenom = form.cleaned_data['prenom']
		sexe = form.cleaned_data['sexe']
		tel = form.cleaned_data['tel']
		mail = form.cleaned_data['mail']
		dateNaissance = form.cleaned_data['dateNaissance']


	utilisateurs=Utilisateur.objects.all()
    # Quoiqu'il arrive, on affiche la page du formulaire.
	return render(request, 'utils.html', locals())

