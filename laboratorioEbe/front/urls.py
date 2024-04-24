from django.urls import path
from . import views



urlpatterns = [
    
    path("", views.login, name="login"),
    path("menu", views.menu, name="menu"),
    path("cuadro", views.cuadro, name="cuadro"),
    path("registro", views.registro, name="registro"),
    path("menu", views.menu, name="menu"),
    path("mPerfil", views.mPerfil, name="mPerfil"),
    path("editarPerfil", views.editarPerfil, name="editarPerfil"),
    path("infSimulacion", views.infSimulacion, name="infSimulacion"),
    path("infEjecucion", views.infEjecucion, name="infEjecucion"),
    path("herAnotacion", views.herAnotacion, name="herAnotacion"),


]
