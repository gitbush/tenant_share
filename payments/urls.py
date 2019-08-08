from django.urls import path
from . import views

urlpatterns = [
    path('', views.payments_list, name='payments-list'),
    path('delete/<int:id>', views.delete_payment, name='payments-delete'),

]