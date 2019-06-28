from django.shortcuts import render, redirect
from .forms import UserRegisterForm, RegisterAsForm, UserUpdateForm, ProfileUpdateForm
from .models import *

def register(request):
    """
        Create a user through registration form. Get type of user from 
        RegisterAsForm and save to previously created user.
    """
    if request.method == 'POST':
        registerForm = UserRegisterForm(request.POST)
        asForm = RegisterAsForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            if asForm.is_valid():
                profile = Profile.objects.filter(user__email=registerForm.cleaned_data['email']).first()
                register_as = asForm.cleaned_data['register_as']
                profile.register_as = register_as
                profile.save()
            return redirect('login')
    else:
        registerForm = UserRegisterForm()
        asForm = RegisterAsForm()
    return render(request, 'users/register.html', {'registerForm': registerForm, 'asForm': asForm})

def account(request, id):
    """
    User account page
    """
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_img_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_update_form.is_valid() and profile_img_form.is_valid():
            user_update_form.save()
            profile_img_form.save()
            return redirect('account', id=request.user.id)
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_img_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_update_form': user_update_form,
        'profile_img_form': profile_img_form,
    }

    return render(request, 'users/account.html', context)
