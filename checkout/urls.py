from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:payment_id>', views.checkout, name='checkout')
]