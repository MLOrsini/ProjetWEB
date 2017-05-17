from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Utilisateurs, name='Utilisateur'),
	url('monProfil/(?P<id>\d+)', views.monProfil, name='monProfil'),
	url(r'^delete$', views.deleteUser, name='delete')


]
