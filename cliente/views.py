from django.shortcuts import render, redirect
from . import models
from datetime import date


def cliente_views(request):
    clientes = models.Registro.objects.all()
    context = {"clientes": clientes}
    return render(request, "cliente/index.html", context)

def crear_usuario(request):
    c1 = models.Registro(nombre="Juana", apellido="Villareal", nacimiento=date(2015, 1, 1))
    c2 = models.Registro(nombre="Francisco", apellido="Furtado", nacimiento=date(2005, 2, 2))
    c1.save()
    c2.save()

    return redirect("cliente:index")