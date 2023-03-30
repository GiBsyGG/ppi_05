from django.db import models
from django.utils import timezone
from restaurantes.models import Restaurante
from menus.models import Menu


# Create your models here.
class Pedido(models.Model):
    fecha = models.DateTimeField(default=timezone.now)

    id_restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    id_menu = models.ForeignKey(Menu, on_delete=models.CASCADE)