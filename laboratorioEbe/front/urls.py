from django.urls import path
from . import views



urlpatterns = [
    
    path("", views.index, name="menu"),
    path("cuadro", views.cuadro, name="cuadro"),

]