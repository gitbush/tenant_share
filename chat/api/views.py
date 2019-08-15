from rest_framework import viewsets
from django.db.models import Q
from chat.models import ChatMessage
from maintenance.models import MaintRequest, Rental
from .serializers import ChatMessageSerializer

# api view for chat messages
class ChatMessageView(viewsets.ModelViewSet):
    """
    Chat messages api view
    Alter queryset to handle ajax requests with relevant maintenance request ID.
    """
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

    def get_queryset(self, *args, **kwargs):
        """
        get_queryset to handle url parameters
        """
        query = self.request.GET.get('q')
        last_msg_id = self.request.GET.get('id')
        if query and last_msg_id: # if parameters in url
            queryset = ChatMessage.objects.filter(Q(maint_request=query)&
                                       Q(id__gt=last_msg_id))
            
        else:
            queryset = ChatMessage.objects.all()

        return queryset

    # save current user to chat message on create via api
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

