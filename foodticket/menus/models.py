from django.db import models
from restaurantes.models import RestauranteUsuario
# Create your models here.
class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.IntegerField()
    DIA1_OPCIONES = (
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
        ('Diario', 'Diario'),
    )
    DIA2_OPCIONES = (
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    )
    DIA3_OPCIONES = (
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    )
    dia1 = models.CharField(max_length=10, choices=DIA1_OPCIONES)
    dia2 = models.CharField(max_length=10, choices=DIA2_OPCIONES, blank=True)
    dia3 = models.CharField(max_length=10, choices=DIA3_OPCIONES, blank=True)

    id_restaurante = models.ForeignKey(RestauranteUsuario, on_delete=models.CASCADE)



