from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/login.html'), name='logout'),
    path('account/<int:id>', views.account, name='account'),
    path('tenant/add/<int:rental_id>', views.add_tenant, name='add-tenant'),
    path('tenant/remove/<int:rental_id>/<int:id>', views.remove_tenant, name='remove-tenant'),
    path('password/', include('django.contrib.auth.urls')),
]