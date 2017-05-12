from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.evenement),
    url(r'^ev/(?P<id>[0-9]+)$', views.detailevenement),
    #url(r'^ev/1$', views.detailevenement),
]
