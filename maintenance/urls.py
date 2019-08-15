from django.urls import path
from . import views

urlpatterns = [
    path('home', views.Home, name='maint-home'),
    path('maintenance', views.MaintRequestList, name='maint-list'),
    path('maintenance/request/<int:id>/', views.MaintRequestDetail, name='maint-detail'),  
    path('maintenance/new', views.MaintRequestCreate, name='maint-create'),
    path('maintenance/delete/<int:id>', views.MaintRequestDelete, name='maint-delete'),
]