from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("inicio/", include("home.urls")),  #LA url de google se modifica en ESTE archivo (ProyFin)
    path("cliente/", include("cliente.urls")),
]

