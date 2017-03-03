# -*- coding: utf 8 -*-
from django.db import models
from django.contrib.auth.models import User, Permission
from django.utils import timezone

class Nota(models.Model):
	usuario = models.ForeignKey(User),
	nota = models.CharField(max_length=100, verbose_name='Nota', blank=False),
	data = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.nota