from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('new_gasto/', views.new_gasto, name='new_gasto'),
    path('get_gastos/', views.get_gastos, name='get_gastos'),
    path('get_debts/', views.get_debts, name='get_debts'),
    path('pay_debt/<int:debt_id>/', views.pay_debt, name='pay_debt'),
    #Editar gastos

]
