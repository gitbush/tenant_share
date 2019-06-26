from django.shortcuts import render
from django.http import HttpResponse
from .models import MaintRequest


def Home(request):
    currentUser = request.user
    context = {
        'userLandlord': currentUser.profile.rental.landlord,
        'userRental': currentUser.profile.rental 
    }
    return render(request, 'maintenance/home.html', context)

def MaintRequestList(request):
    return render(request, 'maintenance/maint_requests.html')

def MaintRequestDetail(request):
    return render(request, 'maintenance/maint_detail.html')