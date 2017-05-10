from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.profil),
	url('Utilisateur', views.Utilisateur, name='Utilisateur'),
	url('monProfil', views.monProfil)
]
