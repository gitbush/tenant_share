from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Home page</h1>')

def maint_list(request):
    return HttpResponse('<h1>Maintenance List Page</h1>')