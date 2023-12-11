from django.urls import path, include
from . import views

app_name = "cliente"

urlpatterns = [
    path ("", views.cliente_views, name = "index"),
    path ("clientes_creados/", views.crear_usuario, name = "crear_usuario"),
]
