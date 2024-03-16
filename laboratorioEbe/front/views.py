from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
#imprime un txto html
def index(request):
    template = loader.get_template("front/index.html")
    context = {}
    return HttpResponse(template.render(context,request))
    #return render(request, "front/index.html", context)


