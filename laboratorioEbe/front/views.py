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
def gPerfil(request):
    context = {}
    return render(request, 'front/GPerfil.html', context)

