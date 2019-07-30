from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, RegisterAsForm, UserUpdateForm, ProfileUpdateForm
from .models import *
from maintenance.forms import RentalCreationForm

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
                profile = Profile.objects.filter(user__username=registerForm.cleaned_data['username']).first()
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
    User account page with profile editor and rental property editor
    """
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_img_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        rental_form = RentalCreationForm(request.POST, request.FILES, instance=request.user.profile.rental)

    # check which form is submitted 
        if 'profile' in request.POST:
            if user_update_form.is_valid() and profile_img_form.is_valid():
                user_update_form.save()
                profile_img_form.save()
                return redirect('account', id=request.user.id)
        elif 'rental' in request.POST:
            user_profile = get_object_or_404(Profile, user=request.user)
            if rental_form.is_valid():
                new_rental = rental_form.save(commit=False)
                new_rental.landlord = request.user
                new_rental.save()
                user_profile.rental = new_rental
                user_profile.save()
                return redirect('account', id=request.user.id)
    # populate boths forms on GET
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_img_form = ProfileUpdateForm(instance=request.user.profile)
        rental_form = RentalCreationForm(instance=request.user.profile.rental)

    context = {
        'user_update_form': user_update_form,
        'profile_img_form': profile_img_form,
        'rental_form': rental_form,
    }

    return render(request, 'users/account.html', context)


def add_tenant(request, id):
    """
    Register a new user and add to the current rental property.
    """

    current_rental = get_object_or_404(Rental, id=id)
    
    if request.method == 'POST':
        registerForm = UserRegisterForm(request.POST)
        asForm = RegisterAsForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            if asForm.is_valid():
                profile = Profile.objects.filter(user__username=registerForm.cleaned_data['username']).first()
                register_as = asForm.cleaned_data['register_as']
                profile.register_as = register_as
                profile.rental = current_rental
                profile.save()
            return redirect('maint-home')
    else:
        registerForm = UserRegisterForm()
        asForm = RegisterAsForm()
    return render(request, 'users/add_tenant.html', {'registerForm': registerForm, 'asForm': asForm})