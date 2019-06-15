from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first = forms.CharField(label='First Name')
    last = forms.CharField(label='Last Name')

    class Meta:
        model = User
        fields = ['first', 'last', 'username', 'email', 'password1', 'password2']