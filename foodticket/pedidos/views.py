from django.shortcuts import render
from django.views import generic

# Create your views here.

# Para crear la primera vista del home
class IndexView(generic.TemplateView):
    template_name = "pedidos/index.html"


def Historial(request):
    """Vista para la revisión del historial de pedidos"""
    # TODO: Implementar vista para el historial de pedidos
    return render(request, "pedidos/historial.html")