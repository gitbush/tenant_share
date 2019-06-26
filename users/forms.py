from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# register as field choices
register_choices = ((None, 'Select'),('Landlord', 'Landlord'), ('Tenant', 'Tenant'))

# register form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

# form to handle register as option on register page
class RegisterAsForm(forms.Form):
    register_as = forms.ChoiceField(label='Register as', choices= register_choices)
