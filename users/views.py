from django.shortcuts import render, redirect
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        registerForm = UserRegisterForm(request.POST)
        if registerForm.is_valid():
            return redirect('maint-home')
    else:
        registerForm = UserRegisterForm()
    return render(request, 'users/register.html', {'registerForm': registerForm})
