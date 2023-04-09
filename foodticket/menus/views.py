from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.db import IntegrityError


from .models import Menu
from  restaurantes.models import RestauranteUsuario
# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "menus/index.html"

def crear_menu(request):
    """Crea un menú para el restaurante del usuario que está con la sesión iniciada"""
    if request.method == "GET":
        return render(request, "menus/crear_menu.html")
    else:
        try:
            # Buscamos el restaurante del usuario que está creando el menú
            restaurante = get_object_or_404(RestauranteUsuario, usuario=request.user)
            menu = Menu.objects.create(
                nombre=request.POST["menu_nombre"],
                descripcion=request.POST["menu_descripcion"],
                precio=request.POST["menu_precio"],
                dia1=request.POST["menu_dia1"],
                dia2=request.POST["menu_dia2"],
                dia3=request.POST["menu_dia3"],
                id_restaurante=restaurante
                )
            
            # Guardamos el menú en la base de datos
            menu.save()

            # Redirigimos al usuario a la página de menus
            return redirect("menus:index")
        except IntegrityError:
            return render(request, "menus/crear_menu.html", {
                "error": "Menú ya creado"
            })
