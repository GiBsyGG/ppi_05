from django import forms

class FormularioVentaTiquetera(forms.Form):
    nombre = forms.CharField(label="Nombre")
    cedula = forms.CharField(label="Cedula", required=True)
    cantidad = forms.IntegerField(label="Cantidad", required=True)

class FormularioVentaAlmuerzo(forms.Form):
    cedula = forms.CharField(label="Cedula", required=True)
    cantidad = forms.IntegerField(label="Cantidad", required=True)

