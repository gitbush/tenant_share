from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets
from .models import ChatMessage
from maintenance.models import MaintRequest, Rental
from .serializers import ThreadSerializer, ChatMessageSerializer
from django.views.decorators.csrf import csrf_exempt
    
def GetMessages(request, id):

    """
    Get all messages related to current maintenance request.
    """
    maint_request = get_object_or_404(MaintRequest, id=id)
    messages = ChatMessage.objects.filter(maint_request=maint_request)

    context = {
        'messages': messages,
    }

    return render(request, 'maintenance/request_messages.html', context)

# api view for chat messages
class ChatMessageView(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = ChatMessage.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(maint_request=query)
        return queryset

