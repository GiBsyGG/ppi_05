from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('compra/', views.compra, name="compra"),
    path('venta/', views.venta, name="venta"),

]