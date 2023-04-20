from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from .forms import FormularioVentaTiquetera,FormularioVentaAlmuerzo, ClienteForm, TiqueteraForm
from .models import Cliente, Tiquetera
from restaurantes.models import RestauranteUsuario

# Create your views here.

#TODO: Agregar validaciones de login

def index(request):
    return render(request, "clientes/index.html")

def venta(request):

    formulario = FormularioVentaTiquetera()

    if request.method == 'POST':

        formulario = FormularioVentaTiquetera(data=request.POST)
        restaurante = RestauranteUsuario.objects.get(usuario=request.user)

        if formulario.is_valid():
            nombre = request.POST.get("nombre")
            cedula = request.POST.get("cedula")
            cantidad = request.POST.get("cantidad")
        
        # Si el cliente no existe debe crearse
        try:
            clienteForm = ClienteForm(data=request.POST)
            tiqueteraForm = TiqueteraForm(data=request.POST)

            cliente = clienteForm.save(commit=False)
            tiquetera = tiqueteraForm.save(commit=False)


            cliente.id_restaurante = restaurante
            tiquetera.id_restaurante = restaurante
            tiquetera.id_cliente = cliente
            # Se debe guardar el cliente y la tiquetera
            cliente.save()
            tiquetera.save()

        # Si el cliente ya existe se debe recuperar para asiganrle la tiquetera
        except:
            cliente = Cliente.objects.get(cedula=cedula)
            tiqueteraForm = TiqueteraForm(data=request.POST)

            tiquetera = tiqueteraForm.save(commit=False)
            tiquetera.id_restaurante = restaurante
            tiquetera.id_cliente = cliente
            # Se debe guardar el cliente y la tiquetera
            cliente.save()
            tiquetera.save()
        
        return redirect("clientes:index")
    else:
        return render(request, "clientes/venta.html", {"formulario_venta": formulario})


def compra(request):

    formulario = FormularioVentaAlmuerzo()
    restaurante = RestauranteUsuario.objects.get(usuario=request.user)

    if request.method == 'POST':

        try:
            cliente = Cliente.objects.get(cedula=request.POST.get("cedula"), id_restaurante = restaurante)
            tiqueteras = Tiquetera.objects.filter(id_cliente=cliente, id_restaurante = restaurante)

            print(list(tiqueteras))
            return redirect("clientes:seleccionar_tiquetera", cliente_id=cliente.id)
        
        except ObjectDoesNotExist:
            return render(request, "clientes/compra.html",
                            {"error": "El cliente no existe"}
                            )
    
    else:
        return render(request, "clientes/compra.html", {"formulario_compra": formulario})


def seleccionar_tiquetera(request, cliente_id):

    restaurante = RestauranteUsuario.objects.get(usuario=request.user)
    tiqueteras = Tiquetera.objects.filter(id_restaurante = restaurante, id_cliente = cliente_id)
    cliente = Cliente.objects.get(id=cliente_id, id_restaurante = restaurante)
    
    if request.method == 'POST':
            tiquetera = Tiquetera.objects.get(pk=request.POST.get("tiquetera_select"), id_restaurante = restaurante, id_cliente = cliente)

            # Se debe validar que la cantidad de tiquetes sea suficiente
            if tiquetera.cantidad - tiquetera.redimidos >= int(request.POST.get("cantidad")):
                tiquetera.redimidos += int(request.POST.get("cantidad"))

                # Si se iguala la cantidad de tiquetes a la cantidad de tiquetes redimidos se debe eliminar la tiquetera
                if tiquetera.cantidad == tiquetera.redimidos:
                    tiquetera.delete()
                else:
                    tiquetera.save()
            else:
                return render(request, "clientes/seleccionTiquetera.html",
                            {"error": "No hay suficientes tiquetes para realizar la compra", 
                            "tiqueteras": tiqueteras, "cliente": cliente}
                            )
            
            return render(request, "clientes/seleccionMenu.html",{
                "cliente": cliente, "menus": restaurante.menu_set.all(),
                "cantidad": [i for i in range(int(request.POST.get("cantidad")))]
                })
    else:
        return render(request, "clientes/seleccionTiquetera.html", 
                        {"tiqueteras": tiqueteras, "cliente": cliente})

def seleccionar_menu(request, cliente_id):

    restaurante = RestauranteUsuario.objects.get(usuario=request.user)
    cliente = Cliente.objects.get(id=cliente_id, id_restaurante = restaurante)
    menus = restaurante.menu_set.all()
    
    if request.method == 'POST':
        menus_seleccionados = dict(request.POST.items())
        menus_seleccionados.pop("csrfmiddlewaretoken")
        print(menus_seleccionados)
        #TODO: Se debe guardar la compra en la base de datos, usaremos la app pedidos para esto


        return redirect("clientes:index")
    else:
        return render(request, "clientes/seleccionMenu.html", 
                        {"menus": menus, "cliente": cliente})