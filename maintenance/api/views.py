from django.shortcuts import render
from rest_framework import viewsets

from .serializers import MaintenanceRequestSerializer
from maintenance.models import MaintRequest


class MaintListApiView(viewsets.ModelViewSet):
    """
    Maintenance request api view
    """
    queryset = MaintRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer