from django.shortcuts import render, redirect
from . import models
from . import forms
from django.urls import reverse_lazy
# Create your views here.

def productos_views(request):
    productos = models.Productos.objects.all()
    context = {"productos": productos}
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


def eliminar_producto(req, id):

    if req.method == 'POST':

        producto = models.Productos.objects.get(id=id)
        producto.delete()

        productos = models.Productos.objects.all()

        return render(req, "productos/index.html", {"productos": productos})


def editar_producto(req, id):

    producto = models.Productos.objects.get(id=id)

    if req.method == 'POST':
        miFormulario = forms.ProductoForm (req.POST, instance= producto)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            models.Productos.producto = data["producto"]
            models.Productos.precio = data["precio"]
            producto.save()

            return redirect("productos:index")
        
        return render(req, "productos/update.html", {"miFormulario": miFormulario, "producto":producto})

    else:

        miFormulario = forms.ProductoForm(initial={
            "producto": models.Productos.producto,
            "precio": models.Productos.precio
        })

        return render(req, "productos/update.html", {"miFormulario": miFormulario, "id": producto.id})    

  

