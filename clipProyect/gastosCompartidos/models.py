from django.db import models
from users.models import User
from enum import Enum

import datetime
    
class Gasto(models.Model):

    title = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=255, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    date = models.DateTimeField(null=False, default= datetime.datetime.now())
    pay_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gastos_pagados')
    participantes = models.ManyToManyField(User, related_name='gastos_participados')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title

class DebtState(models.TextChoices):
    PENDIG = ('P', 'Pendiente')  # Use a tuple for better readability (optional)
    COMPLETE = ('C', 'Pagada')
    DELETED = ('D', 'Eliminada')

class Debt(models.Model):
    debtor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Debts_como_debedor')
    creditor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Debts_como_acreedor')
    gasto = models.ForeignKey(Gasto, on_delete=models.CASCADE, related_name='gasto')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=DebtState.choices, default=DebtState.PENDIG)
    payment_date = models.DateTimeField(null=True, blank=True)  # Opcional, para registrar la fecha de pago

    def __str__(self):
        return f"{self.debtor} le debe ${self.total} a {self.creditor} por el gasto {self.gasto}"


