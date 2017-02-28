from django.db import models
from django.contrib.auth.models import User, Permission

class Nota(models.Model):
	nota = models.CharField(max_length=100, verbose_name='Nota', blank=False)

	def __str__(self):
		return self.nota