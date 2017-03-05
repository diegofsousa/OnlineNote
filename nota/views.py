# -*- coding: utf 8 -*-
from django.shortcuts import render, HttpResponse, redirect, Http404
from django.contrib.auth import login, logout, authenticate
from .models import User, Nota
import json


def home(request):
	if not request.user.is_authenticated(): return login_user(request)
	return render(request, 'nota/index.html',
	{
		'nota':Nota.objects.all()[::-1]
	})

def login_user(request):
	return render(request, 'nota/login.html')

def entrar(request):
	if request.method == 'POST' and request.is_ajax():
		user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponse(json.dumps(True), content_type="application/json")
		return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404


def register(request):
	if request.method == 'POST' and request.is_ajax():
		userInstance = User()
		userInstance.username = request.POST.get('username')
		userInstance.email = request.POST.get('email')
		passw = request.POST.get('password')
		userInstance.set_password(passw)
		userInstance.save()
		print("user: "+ userInstance.username)
		print("senha: "+ passw)
		user = authenticate(username=userInstance.username, password=passw)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponse(json.dumps(True), content_type="application/json")
		return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404

def make_logout(request):	
	logout(request)
	return redirect("/")

def delete_account(request):
	if request.is_ajax():
		request.user.delete()
		return HttpResponse(json.dumps(True), content_type="application/json")
	raise Http404

def add(request):
	if request.method == 'POST' and request.is_ajax():
		try:
			if request.POST.get('value') != "":
				noteInstance = Nota()
				noteInstance.texto = request.POST.get('value')
				noteInstance.usuario = request.user
				noteInstance.save()
				return HttpResponse(json.dumps(True), content_type="application/json")
			return HttpResponse(json.dumps(False), content_type="application/json")
		except Exception as e:
			return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404