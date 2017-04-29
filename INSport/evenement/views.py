from django.shortcuts import render
from evenement.models import Article

#from django.http import HttpResponse
# Create your views here.

def evenement(request):
    exemple=Article(titre="Bonjour", auteur="Flavien", contenu="Salut")
    print(exemple.titre)
    exemple.save()
    return render(request,'evenement.html')
	#return HttpResponse("bonjour {{exemple.auteur}}")
