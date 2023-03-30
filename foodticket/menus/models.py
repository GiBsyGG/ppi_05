from django.db import models

# Create your models here.
class Menus(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    DIA_OPCIONES = (
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo')
    )
    dia = models.CharField(max_length=10, choices=DIA_OPCIONES)

    id_restaurante = models.ForeignKey(Restaurantes, on_delete=models.CASCADE)



