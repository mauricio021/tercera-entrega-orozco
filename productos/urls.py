from django.urls import path, include
from . import views

app_name = "productos"

urlpatterns = [
    path ("", views.productos_views, name = "index"),
    path ("crear/", views.crear, name = "crear")
]
