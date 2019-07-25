from django.urls import path, include
from . import views

urlpatterns = [
    path('get-messages/<int:id>/', views.GetMessages, name='get-messages'),
]