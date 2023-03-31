from django.shortcuts import render
from django.views import generic

# Create your views here.

# Para crear la primera vista del home
class IndexView(generic.TemplateView):
    template_name = "restaurantes/index.html"