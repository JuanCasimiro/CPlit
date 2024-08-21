from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # Ensures user is logged in
from django.contrib import messages
from .forms import GastoForm
import decimal
from .models import Gasto, Debt



def new_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            # Datos válidos, guardar en la base de datos
            gasto = form.save()
            creditor = form.cleaned_data['pay_by']
            debtors_list = form.cleaned_data['participantes']
            total = form.cleaned_data['total']

            # Eliminar al acreedor de la lista de deudores si está presente
            debts_list = [deudor for deudor in debtors_list if deudor != creditor]

            # Calcular el monto por deudor
            cantidad_deudores = len(debtors_list)
            total_per_debtor = decimal.Decimal(total / cantidad_deudores)
            
            # Crear las deudas
            for deudor in debts_list:
                deuda = Debt(
                    debtor=deudor,
                    creditor=creditor,
                    total=total_per_debtor,
                    gasto=gasto,
                )
                deuda.save()


            return redirect('get_gastos')  # Redirige a la vista del gasto creado
    else:
        form = GastoForm()
    return render(request, 'class_form.html', {'form': form})


def get_gastos(request):
    gastos = Gasto.objects.order_by('-date')
    return render(request, 'lista_gastos.html', {'gastos': gastos})

def get_debts(request):
    debts = Debt.objects.filter(status='P').order_by('-date')
    return render(request, 'debts_list.html', {'debts': debts})

def pay_debt(request, debt_id):
    debt = Debt.objects.get(id=debt_id)  # Utiliza get para obtener el objeto Debt

    # Marcar la deuda como pagada
    debt.status = "C"  
    debt.save()

    # Redirigir a una vista de éxito o a la lista de deudas
    return redirect('get_debts')