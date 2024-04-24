from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
#imprime un txto html
def login(request):
    template = loader.get_template("front/login.html")
    context = {}
    return HttpResponse(template.render(context,request))
def menu(request):
    context = {}
    return render(request, 'front/menu.html', context)

def cuadro(request):
    context = {}
    return render(request, 'front/cuadro_formulario.html', context)
def registro(request):
    context = {}
    return render(request, 'front/registro.html', context)
def mPerfil(request):
    context = {}
    return render(request, 'front/mPerfil.html', context)
def editarPerfil(request):
    context = {}
    return render(request, 'front/editarPerfil.html', context)
def infSimulacion(request):
    context = {}
    return render(request, 'front/infSimulacion.html', context)
def infEjecucion(request):
    context = {}
    return render(request, 'front/infEjecucion.html', context)
def herAnotacion(request):
    context = {}
    return render(request, 'front/herAnotacion.html', context)
