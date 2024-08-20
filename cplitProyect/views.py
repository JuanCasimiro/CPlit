from django.http import HttpResponse    
from django.shortcuts import render
from .models import Gasto


def index(request):
    return HttpResponse("<h1>Hola Pepe</h1>")

def lista_gastos(request):
    gastos = Gasto.objects.all()
    return render(request, 'gastos/lista_gastos.html', {'gastos': gastos})
