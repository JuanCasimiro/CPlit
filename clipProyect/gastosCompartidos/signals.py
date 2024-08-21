from django.db.models.signals import post_save
from django.db.models import Sum
from django.dispatch import receiver
from .models import Debt, DebtState
import datetime


@receiver(post_save, sender=Debt)
def update_user_balance(sender, instance, created, **kwargs):
    if created:
        debtor = instance.debtor
        debtor.balance -= instance.total
        debtor.save()
    if instance.status == DebtState.PENDIG:
        debtor = instance.debtor
        debts = Debt.objects.filter(debtor=debtor, status=DebtState.PENDIG)
        total_debt = debts.aggregate(total=Sum('total'))['total'] or 0
        debtor.balance = -total_debt
        debtor.save()
    if instance.status == DebtState.COMPLETE or instance.status == DebtState.DELETED:
        if instance.status == DebtState.COMPLETE:
            instance.payment_date= datetime.datetime.now()
        debtor = instance.debtor
        debtor.balance = debtor.balance + instance.total
        debtor.save()
    
