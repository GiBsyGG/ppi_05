from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)

    id_restaurante = models.ForeignKey(Restaurantes, on_delete=models.CASCADE)
