from django import forms
from django.db.models import Q
from .models import Payment
from maintenance.models import MaintRequest

class PaymentForm(forms.ModelForm):
    """
    New payment form
    """
    class Meta:
        model = Payment
        fields = ['maint_request', 'amount']
        widgets = {
          'maint_request': forms.Select(attrs={'class': 'form-height'}),
                                              
        }

    # set maint_request choices to get from current user rental
    def __init__(self, property_ref, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['maint_request'].queryset = MaintRequest.objects.filter(Q(property_ref=property_ref) & ~Q(status='resolved'))
