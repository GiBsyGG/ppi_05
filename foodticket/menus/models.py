from django.db import models
from restaurantes.models import RestauranteUsuario
# Create your models here.
class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    lunes = models.BooleanField(default=False)
    martes = models.BooleanField(default=False)
    miercoles = models.BooleanField(default=False)
    jueves = models.BooleanField(default=False)
    viernes = models.BooleanField(default=False)
    sabado = models.BooleanField(default=False)
    domingo = models.BooleanField(default=False)

    id_restaurante = models.ForeignKey(RestauranteUsuario, on_delete=models.CASCADE)



