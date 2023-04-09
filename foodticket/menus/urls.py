from django.contrib import admin
from django.urls import path

from . import views

app_name = "menus"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("crear/", views.crear_menu, name="crear_menu"),
]