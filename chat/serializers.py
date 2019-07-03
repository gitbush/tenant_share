from rest_framework import serializers
from .models import ChatMessage, Thread

# serializers for thread and chat models api
class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ('id', 'rental', 'maint_request')

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ('id', 'thread', 'author', 'message', 'date_posted')
