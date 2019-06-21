from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='maint-home'),
    path('maintenance', views.MaintRequestList, name='maint-list'),
    path('maintenance/request', views.MaintRequestDetail, name='maint-detail'),    # edit with id when set up
]