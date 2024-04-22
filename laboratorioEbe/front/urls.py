from django.urls import path
from . import views



urlpatterns = [
    
    path("", views.login, name="login"),
    path("menu", views.menu, name="menu"),
    path("cuadro", views.cuadro, name="cuadro"),
    path("registro", views.registro, name="registro"),
    path("menu", views.menu, name="menu"),
    path("gPerfil", views. gPerfil, name="gPerfil"),

]