from django.shortcuts import render
from rest_framework import viewsets

from .serializers import UserSerializer
from users.models import User

# Create your views here.

class UserListApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self, *args, **kwargs):
        """
        get_queryset to handle url parameters
        """
        query = self.request.GET.get('q')
        if query: # if parameters in url
            queryset = User.objects.filter(username__startswith=query)
            
        else:
            queryset = User.objects.all()

        return queryset