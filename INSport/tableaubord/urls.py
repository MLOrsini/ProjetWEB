from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tableaubord,name='tableaubord'),
    url(r'^utils/$', views.utils,name='utils'),
]
