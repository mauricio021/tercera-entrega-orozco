from django.shortcuts import render, redirect
from . import models
from . import forms
from datetime import date

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


def buscar_cliente(request):
    if request.method == "GET":
        form = forms.RegistroBusqueda()
        context = {"form" : form}
        return render (request, "cliente/busqueda.html", context)

    #else:
        # formulario = forms.RegistroBusqueda(request.POST)
        # if formulario.is_valid():
        #     informacion = formulario.cleaned_data
        #     cliente_filtrados = models.Registro.objects.filter(cliente=informacion["nombre"])
        #     contexto = {"cliente_filtrados": cliente_filtrados}
        #     return render(request, "cliente/index.html", contexto)



        # formulario = forms.RegistroBusqueda(request.POST)
        # if formulario.is_valid():
        #     informacion = formulario.cleaned_data
        #     cliente_filtrados = []
        #     for i in models.Registro.objects.filter(cliente=informacion["nombre"]):
        #         cliente_filtrados.append(i)
        #     contexto = {"cliente": buscar_cliente}
        #     return render (request, "cliente/index.html", contexto)
        
    elif request.method == "POST":            
        form = forms.RegistroBusqueda(request.POST)
        if form.is_valid():
            datos_formulario = form.cleaned_data
            models.Registro = models.Registro.objects.create(**datos_formulario)
            return redirect("cliente:index")
        else:
            print ("error")


def eliminar_cliente(req, id):

    if req.method == 'POST':

        cliente = models.Registro.objects.get(id=id)
        cliente.delete()

        clientes = models.Registro.objects.all()

        return render(req, "cliente/index.html", {"clientes": clientes})


def editar_cliente(req, id):

    cliente = models.Registro.objects.get(id=id)

    if req.method == 'POST':
        miFormulario = forms.RegistroForm(req.POST, instance=cliente)

        if miFormulario.is_valid():       
            miFormulario.save()

            return redirect("cliente:index")
        
        return render(req, "cliente/editar.html", {"miFormulario": miFormulario, "cliente": cliente})

    else:

        miFormulario = forms.RegistroForm(            
            initial={
                "nombre": models.Registro.nombre,
                "apellido": models.Registro.apellido,
            })

        return render(req, "cliente/editar.html", {"miFormulario": miFormulario, "cliente": cliente})    
    

