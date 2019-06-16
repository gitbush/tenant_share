from django.shortcuts import render
from django.http import HttpResponse
from .models import MaintRequest


def home(request):
    requests = MaintRequest.objects.all()
    return render(request, 'maintenance/home.html', {'requests': requests})

def maint_list(request):
    return HttpResponse('<h1>Maintenance List Page</h1>')