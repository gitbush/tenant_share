from django.shortcuts import render
from django.http import HttpResponse
from .models import Maint_request


def home(request):
    requests = Maint_request.objects.all()
    return render(request, 'maintenance/home.html', {'requests': requests})

def maint_list(request):
    return HttpResponse('<h1>Maintenance List Page</h1>')