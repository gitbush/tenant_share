from django import forms
from .models import Payment
from maintenance.models import MaintRequest

class PaymentForm(forms.ModelForm):
    
    class Meta:
        model = Payment
        fields = ['maint_request', 'amount']
