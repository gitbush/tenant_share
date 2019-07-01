from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def Home(request):
    currentUser = request.user
    try: 
        userRental = currentUser.profile.rental
        userLandlord = userRental.landlord
        userTenants = userRental.profile_set.filter(register_as='Tenant').all()
        # print(userRental.profile_set.filter(register_as='Tenant').all())
        # print(currentRental.profile_set.filter(register_as='Tenant').all())

        context = {
            'userProfile': currentUser.profile,
            'userRental': userRental, 
            'userLandlord': userLandlord,
            'userTenants': userTenants
        }
    except:
        context = {
            'userProfile': currentUser.profile,
        }
            
    return render(request, 'maintenance/home.html', context)

def MaintRequestList(request):
    user_rental = request.user.profile.rental
    maintenance_requests = user_rental.maintrequest_set.all()
    context = {
        'maintenance_requests': maintenance_requests
    }
    return render(request, 'maintenance/maint_requests.html', context)

def MaintRequestCreate(request):
    """
    Create maintenance issue relevant to user and user rental
    """

    return render(request, 'maintenance/maint_create.html' )

def MaintRequestDetail(request):
    return render(request, 'maintenance/maint_detail.html')