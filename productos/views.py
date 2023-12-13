from django.shortcuts import render, redirect
from . import models
from . import forms
# Create your views here.

def productos_views(request):
    vendedor = models.Productos.objects.all()
    context = {"vendedor": vendedor}
    return render(request, "productos/index.html", context)

def crear(request):
    if request.method == "POST":
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("productos:index")
    else:
        form = forms.ProductoForm()
    return render(request, "productos/crear.html", {"form": form})
