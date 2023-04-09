from django import forms
from .models import Menu

class MenuForm(forms.ModelForm):
    class Meta:
        # Modelo en el cual estará basado el formulario
        model = Menu
        # Campos que se mostrarán en el formulario
        fields = ["nombre", "descripcion", "precio", "dia1", "dia2", "dia3"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "required": True}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "required": True}),
            "dia1": forms.Select(attrs={"class": "form-control", "required": True}),
            "dia2": forms.Select(attrs={"class": "form-control"}),
            "dia3": forms.Select(attrs={"class": "form-control"}),
        }