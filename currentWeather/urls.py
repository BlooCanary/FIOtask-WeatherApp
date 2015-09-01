from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.weather, name='weather'),
    url(r'^login', views.login, name='login'),
    url(r'^newLocation', views.newLocation, name='newLocation'),
]
