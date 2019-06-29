from django import forms
from .models import Rental


# form to add rental property
class RentalCreationForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['address', 'postcode', 'city', 'no_of_tenants', 'image']