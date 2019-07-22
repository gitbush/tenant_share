from django.shortcuts import render
from rest_framework import viewsets

from .serializers import UserSerializer
from users.models import User

# Create your views here.

class UserListApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer