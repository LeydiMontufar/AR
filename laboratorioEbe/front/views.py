from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
#imprime un txto html
def index(request):
    template = loader.get_template("front/menu.html")
    context = {}
    return HttpResponse(template.render(context,request))
def cuadro(request):
    context = {}
    return render(request, 'front/cuadro_formulario.html', context)

