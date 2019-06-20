from django.shortcuts import render, redirect
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        registerForm = UserRegisterForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            return redirect('maint-home')
    else:
        registerForm = UserRegisterForm()
    return render(request, 'users/register.html', {'registerForm': registerForm})

def account(request):

    return render(request, 'users/account.html')
