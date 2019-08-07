from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets

from .serializers import UserSerializer
from users.models import User, Profile

# Create your views here.

class UserListApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self, *args, **kwargs):
        """
        get_queryset to handle url parameters
        """
        query = self.request.GET.get('q')
        if self.request.is_ajax:
            if len(query) > 0: # if parameters in url
                queryset = User.objects.filter(Q(username__startswith=query)&
                                            Q(profile__rental=None))
                return queryset
        else:
            print(self.request)
            queryset = User.objects.all()

            return queryset