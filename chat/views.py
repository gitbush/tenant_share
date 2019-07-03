from django.shortcuts import render
from rest_framework import viewsets
from .models import ChatMessage, Thread
from .serializers import ThreadSerializer, ChatMessageSerializer

# api view for thread
class ThreadView(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

# api view for chat messages
class ChatMessageView(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer


