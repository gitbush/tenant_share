from django.shortcuts import render
from .forms import UserRegisterForm

def register(request):
    registerForm = UserRegisterForm()
    return render(request, 'users/register.html', {'registerForm': registerForm})
