from rest_framework import serializers
from .models import ChatMessage, Thread
from users.models import User

# serializers for thread and chat models api
class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ('id', 'rental', 'maint_request')

class ChatMessageSerializer(serializers.ModelSerializer):
    # author = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    # thread = serializers.SlugRelatedField(many=False, slug_field='maint_request', queryset=Thread.objects.all())

    class Meta:
        model = ChatMessage
        fields = ('id','maint_request', 'author', 'message', 'date_posted')
