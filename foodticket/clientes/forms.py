from django import forms
from .models import Cliente, Tiquetera
class FormularioVentaTiquetera(forms.Form):
    nombre = forms.CharField(label="Nombre")
    cedula = forms.CharField(label="Cedula", required=True)
    cantidad = forms.IntegerField(label="Cantidad", required=True)
    

class FormularioVentaAlmuerzo(forms.Form):
    cedula = forms.CharField(label="Cedula", required=True)


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "cedula"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "cedula": forms.TextInput(attrs={"class": "form-control", "required": True}),
        }


class TiqueteraForm(forms.ModelForm):
    class Meta:
        model = Tiquetera
        fields = ["cantidad"]
        widgets = {
            "cantidad": forms.NumberInput(attrs={"class": "form-control", "required": True}),
        }