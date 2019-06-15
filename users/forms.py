from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# register as field choices
register_choices = ((None, 'Select'),('Landlord', 'Landlord'), ('Tenant', 'Tenant'))

# register form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first = forms.CharField(label='First Name')
    last = forms.CharField(label='Last Name')
    register_as = forms.ChoiceField(label='Register as', choices= register_choices)

    class Meta:
        model = User
        fields = ['first', 'last', 'username','register_as', 'email', 'password1', 'password2']