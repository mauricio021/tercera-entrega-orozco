from django.shortcuts import render, redirect
from . import models
from datetime import date
from . import forms

def cliente_views(request):
    clientes = models.Registro.objects.all()
    context = {"clientes": clientes}
    return render(request, "cliente/index.html", context)



def crear(request):
    if request.method == "POST":
        form = forms.RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:index")
    else:
        form = forms.RegistroForm()
    return render(request, "cliente/crear.html", {"form": form})