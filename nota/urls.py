from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'nota'

urlpatterns = [
   url(r'^$', views.home, name='home'),
   url(r'^autentica/$', views.entrar),
   url(r'^registra/$', views.register),
   url(r'^deletaconta/$', views.deletaconta),
   url(r'^logout/$', views.make_logout),
   url(r'^add/$', views.add),
   url(r'^remove/$', views.remove),


]