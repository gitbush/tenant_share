from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='maint-home'),
    path('maintenance', views.maint_list, name='maint-list'),
]