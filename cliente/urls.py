from django.urls import path, include
from . import views

app_name = "cliente"

urlpatterns = [
    path ("", views.cliente_views, name = "index"),
    path ("crear/", views.crear, name = "crear"),
]
