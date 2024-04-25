from django.urls import path
from . import views



urlpatterns = [
    
    path("", views.login, name="login"),
    path("menu", views.menu, name="menu"),
    

    path("ejecutar_ca", views.cuadro, name="ejecutar_ca"),
    path('ejecutar_ca/', views.ejecutar_ca, name='ejecutar_ca'),
    path('video_feed/', views.video_feed, name='video_feed'),

    path("registro", views.registro, name="registro"),
    path("menu", views.menu, name="menu"),
    path("mPerfil", views.mPerfil, name="mPerfil"),
    path("editarPerfil", views.editarPerfil, name="editarPerfil"),
    path("infSimulacion", views.infSimulacion, name="infSimulacion"),
    path("infEjecucion", views.infEjecucion, name="infEjecucion"),
    path("herAnotacion", views.herAnotacion, name="herAnotacion"),



]
