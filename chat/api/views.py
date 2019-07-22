from rest_framework import viewsets
from chat.models import ChatMessage
from maintenance.models import MaintRequest, Rental
from .serializers import ThreadSerializer, ChatMessageSerializer

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

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

