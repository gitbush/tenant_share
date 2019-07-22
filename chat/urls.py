from django.urls import path, include
from . import views
from rest_framework import routers

# routers to handle api request methods
router = routers.DefaultRouter()
router.register('chat-message', views.ChatMessageView)

urlpatterns = [
    path('api/', include(router.urls), name='chat-api'),
    path('get-messages/<int:id>/', views.GetMessages, name='get-messages'),
]