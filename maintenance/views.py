from django.shortcuts import render
from django.http import HttpResponse
from .models import MaintRequest


def home(request):
    requests = MaintRequest.objects.all()
    return render(request, 'maintenance/home.html', {'requests': requests})

def maint_requests(request):
    return render(request, 'maintenance/maint_requests.html')