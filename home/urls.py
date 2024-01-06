from django.urls import path, include
from . import views

app_name = "home"

urlpatterns = [
    path("", views.inicio_view, name = "index"),
    path ("about/", views.about_view, name= "about"),
    path ("registro/", views.registro_view, name = "registro")
]
