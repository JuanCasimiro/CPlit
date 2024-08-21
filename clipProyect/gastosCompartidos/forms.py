from django import forms
from .models import User, Gasto

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ('title', 'description', 'total', 'date', 'pay_by', 'participantes','createdBy')

