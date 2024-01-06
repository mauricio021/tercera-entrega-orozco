from django.shortcuts import render, redirect
from . import models
from . import forms
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required

@login_required
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
        context = {"cliente" : form}
        return render (request, "cliente/busqueda.html", context)

       
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



class ClienteUpdate(UpdateView):
    model = models.Registro
    template_name = "cliente/editar.html"
    fields = ["nombre", "apellido"]
    success_url = "/cliente/"