from django import forms
from . import models


class RegistroForm(forms.ModelForm):
    class Meta:
        model = models.Registro
        fields = ["nombre", "apellido","nacimiento", "correo"]