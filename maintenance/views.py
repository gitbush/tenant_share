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
    return render(request, 'maintenance/maint_requests.html')

def MaintRequestDetail(request):
    return render(request, 'maintenance/maint_detail.html')