from django.shortcuts import render
from rest_framework import viewsets

from .serializers import MaintenanceRequestSerializer
from maintenance.models import MaintRequest

# Create your views here.

class MaintListApiView(viewsets.ModelViewSet):
    queryset = MaintRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer