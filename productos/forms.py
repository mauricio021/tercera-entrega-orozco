from django import forms
from . import models


class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Productos
        fields = ["vendedor", "producto","precio", "correo"]


class ProductosBusqueda(forms.Form):
     producto = forms.CharField()