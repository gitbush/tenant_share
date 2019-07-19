from django.urls import path, include
from . import views
from rest_framework import routers

# routers to handle api request methods
router = routers.DefaultRouter()
router.register('thread', views.ThreadView)
router.register('chat-message', views.ChatMessageView)

urlpatterns = [
    path('get-messages/<int:id>/', views.GetMesages, name='get-messages')
]