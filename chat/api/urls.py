from django.urls import path, include
from . import views
from rest_framework import routers

# routers to handle api request methods
router = routers.DefaultRouter()
router.register('chat-message', views.ChatMessageView)

urlpatterns = [
    path('', include(router.urls), name='chat-api'),
]