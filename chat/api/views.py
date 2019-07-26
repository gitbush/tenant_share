from rest_framework import viewsets
from django.db.models import Q
from chat.models import ChatMessage
from maintenance.models import MaintRequest, Rental
from .serializers import ChatMessageSerializer

# api view for chat messages
class ChatMessageView(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = ChatMessage.objects.all()
        query = self.request.GET.get('q')
        last_msg_id = self.request.GET.get('id')
        if query and last_msg_id:
            queryset = queryset.filter(Q(maint_request=query)&
                                       Q(id__gt=last_msg_id))
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

