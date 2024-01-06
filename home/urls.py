from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

app_name = "home"

urlpatterns = [
    path("", views.inicio_view, name = "index"),
    path ("about/", views.about_view, name= "about"),
    path ("registro/", views.registro_view, name = "registro"),
    path ("login/", views.login_view, name = "login"),
    path("logout", LogoutView.as_view(template_name="home/logout.html"), name="logout"),

]
