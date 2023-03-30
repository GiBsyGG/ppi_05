from django.db import models

# Create your models here.
class Restaurantes(models.Model):
    nombre = models.CharField(max_length=100)
    NIT = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    tipo = models.CharField(max_length=100)


