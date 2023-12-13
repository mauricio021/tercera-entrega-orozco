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

# Si es una solicitud POST, procesa los datos del formulario            
        form = forms.RegistroBusqueda(request.POST)
        if form.is_valid():
# Si el formulario es válido, guarda los datos en la base de datos

            datos_formulario = form.cleaned_data

            models.Registro = models.Registro.objects.create(**datos_formulario)

            # Puedes hacer más cosas aquí si es necesario, como redirigir a otra página

            return redirect("cliente:index") # Cambia ‘otra_vista’ a la URL a la que deseas redirigir

        else:
            print ("errorrrr")
            # Si el formulario no es válido, vuelve a mostrar el formulario con errores

            #return render(request, ‘mi_app/mi_template.html’, {‘form’: form})    