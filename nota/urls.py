from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'nota'

urlpatterns = [
   url(r'^$', views.home, name='home'),
   url(r'^autentica/$', views.entrar),
   url(r'^registra/$', views.register),
   url(r'^logout/$', views.make_logout),


]


#login
#lista
#inserir
#excluir
#logout
