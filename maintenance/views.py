from django.shortcuts import render
from django.http import HttpResponse
from .models import MaintRequest


def Home(request):
    requests = MaintRequest.objects.all()
    return render(request, 'maintenance/home.html', {'requests': requests})

def MaintRequestList(request):
    return render(request, 'maintenance/maint_requests.html')

def MaintRequestDetail(request):
    return render(request, 'maintenance/maint_detail.html')