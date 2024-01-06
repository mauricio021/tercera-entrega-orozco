from django.urls import path, include
from . import views
from cliente.views import ClienteUpdate

app_name = "cliente"

urlpatterns = [
    path ("", views.cliente_views, name = "index"),
    path ("crear/", views.crear, name = "crear"),
    path ("buscar/", views.buscar_cliente, name = "buscar"),
    path("eliminar/<int:id>", views.eliminar_cliente, name="elimina-cliente"),
    path("editar-cliente/<pk>", ClienteUpdate.as_view(), name = "editar-cliente"),
]
