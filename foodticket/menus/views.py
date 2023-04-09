from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from .models import Menu
from  restaurantes.models import RestauranteUsuario
from .forms import MenuForm
# Create your views here.

class IndexView(generic.ListView):
    """
    View principal de los menús del restaurante
    
    pasa como contexto los menus del restaurante del usuario que está con la sesión iniciada
    """
    template_name = "menus/index.html"

    context_object_name = "menus_restaurante"

    def get_queryset(self):
        # Si el usuario está autenticado, devolvemos los menús del restaurante del usuario
        if self.request.user.is_authenticated:
            return Menu.objects.filter(id_restaurante__usuario=self.request.user)
    

@login_required
def crear_menu(request):
    """Crea un menú para el restaurante del usuario que está con la sesión iniciada"""
    if request.method == "GET":
        return render(request, "menus/crear_menu.html", {
            "form": MenuForm
        })
    else:
        try:
            # Buscamos el restaurante del usuario que está creando el menú
            restaurante = get_object_or_404(RestauranteUsuario, usuario=request.user)
            menu = Menu.objects.create(
                nombre=request.POST["nombre"],
                descripcion=request.POST["descripcion"],
                precio=request.POST["precio"],
                dia1=request.POST["dia1"],
                dia2=request.POST["dia2"],
                dia3=request.POST["dia3"],
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


@login_required
def eliminar_menu(request, menu_id):
    """Elimina el menú con el id pasado por parámetro"""
    # Buscamos el menú con el id pasado por parámetro
    menu = get_object_or_404(Menu, id=menu_id)

    # Eliminamos el menú
    menu.delete()

    # Redirigimos al usuario a la página de menus
    return redirect("menus:index")


@login_required
def editar_menu(request, menu_id):
    """Edita el menú con el id pasado por parámetro"""
    # Buscamos el menú con el id pasado por parámetro
    menu = get_object_or_404(Menu, id=menu_id)

    if request.method == "GET":
        return render(request, "menus/editar_menu.html", {
            "form": MenuForm(instance=menu),
            "menu": menu
        })
    else:
        try:
            # Actualizamos los datos del menú
            menu.nombre = request.POST["nombre"]
            menu.descripcion = request.POST["descripcion"]
            menu.precio = request.POST["precio"]
            menu.dia1 = request.POST["dia1"]
            menu.dia2 = request.POST["dia2"]
            menu.dia3 = request.POST["dia3"]

            # Guardamos el menú en la base de datos
            menu.save()

            # Redirigimos al usuario a la página de menus
            return redirect("menus:index")
        except IntegrityError:
            return render(request, "menus/editar_menu.html", {
                "error": "Menú ya creado"
            })