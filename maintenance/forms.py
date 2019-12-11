from django import forms
from .models import Rental, MaintRequest


class RentalCreationForm(forms.ModelForm):
    """ Add a rental property """
    
    class Meta:
        model = Rental
        fields = ['address', 'postcode', 'city', 'no_of_tenants', 'image']

class MaintenanceCreationForm(forms.ModelForm):
    """ Add a maintenance request """

    class Meta:
        model = MaintRequest
        fields = ['title', 'details', 'priority', 'image']

class StatusUpdateForm(forms.ModelForm):
    """ Update status of maintenance request """

    class Meta:
        model = MaintRequest
        fields = ['status']

    def __init__(self, *args, **kwargs):
        """ Set no label on status field """

        super(StatusUpdateForm, self).__init__(*args, **kwargs)
        self.fields['status'].label = False

class MaintenanceQuoteForm(forms.ModelForm):
    """ Update maintenance request with a cost/quote """

    class Meta:
        model = MaintRequest
        fields = ['cost', 'invoice_pdf', 'paid_by']

        



