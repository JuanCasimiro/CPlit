from django.http import HttpResponse
from django.shortcuts import render
from gastosCompartidos.models import  Gasto, Debt
from users.models import User


def home(request):
    gastos = Gasto.objects.all()
    debts = Debt.objects.filter(status = 'P')
    users = User.objects.all()
    return render(request, 'home.html', {'gastos': gastos, 'debts': debts, 'users': users})