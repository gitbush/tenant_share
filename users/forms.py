from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# register_as field choices
register_choices = ((None, 'Select'),('Landlord', 'Landlord'), ('Tenant', 'Tenant'))

class UserRegisterForm(UserCreationForm):
    """
    Extend userCreationForm for added fields
    """
    email = forms.EmailField()
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class RegisterAsForm(forms.Form):
    """
    Handle register as option on register page
    """
    register_as = forms.ChoiceField(label='Register as', choices= register_choices)

class UserUpdateForm(forms.ModelForm):
    """
    Edit/update user profile info
    """
    email = forms.EmailField()
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    """
    Update user image
    """
    class Meta:
        model = Profile
        fields = ['profile_image']