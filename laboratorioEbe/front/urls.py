from django.urls import path
from . import views



urlpatterns = [
    
    path("", views.index, name="menu"),
    path("cuadro", views.cuadro, name="cuadro"),
    path("ejecutar_ca", views.cuadro, name="ejecutar_ca"),
    path('ejecutar_ca/', views.ejecutar_ca, name='ejecutar_ca'),
    path('video_feed/', views.video_feed, name='video_feed'),

]