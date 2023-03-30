from django.db import models
from django.utils import timezone

# Create your models here.
class Pedidos(models.Model):
    fecha = models.DateTimeField(default=timezone.now)

    id_restaurante = models.ForeignKey(Restaurantes, on_delete=models.CASCADE)
    id_menu = models.ForeignKey(Menus, on_delete=models.CASCADE)