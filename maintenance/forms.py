from django import forms
from .models import Rental, MaintRequest, MaintRequestImage


# form to add rental property
class RentalCreationForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['address', 'postcode', 'city', 'no_of_tenants', 'image']

# form to create a maintenance request
class MaintenanceCreationForm(forms.ModelForm):
    class Meta:
        model = MaintRequest
        fields = ['title', 'details', 'priority', 'status', 'date_raised']

class MaintenanceImgForm(forms.ModelForm):
    class Meta:
        model = MaintRequestImage
        fields = ['image']
        



