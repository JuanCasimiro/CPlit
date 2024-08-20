from django.http import HttpResponse
from django.shortcuts import render


def hola(request):
    return render(request, 'hola.html', {})

def newGasto(request, monto):
    context = {'monto' : str(monto)}
    return render(request, 'newGasto.html', context)

def newPago(request, envia, recibe, monto):
    return HttpResponse(envia + " pago: " +  str(monto) + " a " + recibe)

def addPersona(request, nombre):
    return HttpResponse("se incorpora " + nombre + " al equipo")
