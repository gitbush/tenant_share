from rest_framework import serializers
from django.utils import timezone
from chat.models import ChatMessage
from users.api.serializers import UserSerializer

class ChatMessageSerializer(serializers.ModelSerializer):
    """
    Serializer for chat message model for api
    """
    author = UserSerializer(read_only=True)
    class Meta:
        model = ChatMessage
        fields = ('id','maint_request', 'author', 'message', 'date_posted')
