from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Pedido, MenuPedido
from restaurantes.models import RestauranteUsuario
# Create your views here.

# Para crear la primera vista del home
class IndexView(generic.TemplateView):
    template_name = "pedidos/index.html"


@login_required
def Historial(request):
    """Vista para la revisión del historial de pedidos"""
    # TODO: Implementar vista para el historial de pedidos
    restaurante = RestauranteUsuario.objects.get(usuario=request.user)
    pedidos = Pedido.objects.prefetch_related('menupedido_set__id_menu').filter(id_restaurante=restaurante)
    return render(request, "pedidos/historial.html", {"pedidos": pedidos})