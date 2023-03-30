from django.db import models
from restaurantes.models import Restaurante

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)

    id_restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
