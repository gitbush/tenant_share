from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'maintenance/home.html')

def maint_list(request):
    return HttpResponse('<h1>Maintenance List Page</h1>')