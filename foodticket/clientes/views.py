from django.shortcuts import render, redirect
from .forms import FormularioVentaTiquetera, FormularioVentaAlmuerzo

# Create your views here.

def index(request):
    return render(request, "clientes/index.html")

def venta(request):

    formulario = FormularioVentaTiquetera()

    if request.method == 'POST':

        formulario = FormularioVentaTiquetera(data=request.POST)

        if formulario.is_valid():
            nombre = request.POST.get("nombre")
            cedula = request.POST.get("cedula")
            cantidad = request.POST.get("cantidad")

        # TODO: se debe hacer el crud

    return render(request, "clientes/venta.html", {"formulario_venta": formulario})

def compra(request):

    formulario = FormularioVentaAlmuerzo()

    if request.method == 'POST':

        formulario = FormularioVentaAlmuerzo(data=request.POST)

        if formulario.is_valid():
            cedula = request.POST.get("cedula")
            cantidad = request.POST.get("cantidad")

        # TODO: se debe hacer el crud

    return render(request, "clientes/compra.html", {"formulario_compra": formulario})



