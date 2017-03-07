# -*- coding: utf 8 -*-
from django.db import models
from django.contrib.auth.models import User, Permission
from django.utils import timezone
import base64

class Nota(models.Model):
	usuario = models.ForeignKey(User)
	texto = models.CharField(max_length=100, verbose_name='Nota', blank=False)
	data = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.texto

	def save(self, *args, **kwargs):
		self.texto = base64.b64encode(self.texto.encode('utf-8'))
		super(Nota, self).save(*args, **kwargs)

def get_list_decoded(user):
	lista = list()
	for i in Nota.objects.filter(usuario=user):lista.append([i.pk, base64.b64decode(i.texto).decode('utf-8'), i.data])
	return lista