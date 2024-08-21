from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import User

def new_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Datos válidos, guardar en la base de datos
            user = form.save()

            return redirect('get_users')  # Redirige a la vista del gasto creado
    else:
        form = UserForm()
    return render(request, 'class_form.html', {'form': form})

def get_users(request):
    users = User.objects.order_by('-name')
    return render(request, 'users_list.html', {'users': users})