from django.conf.urls import url
from . import views

from django.conf.urls import  url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nice/(?P<event_id>\d+)/$', views.nice, name='nice'),
    url(r'^nope/(?P<event_id>\d+)/$', views.nope, name='nope'),
]
