from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500, handler403


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('maintenance.urls')),
    path('', include('users.urls')),
    path('payments/', include('payments.urls')),
    path('checkout/', include('checkout.urls')),
    path('api/chat/', include('chat.api.urls')),
    path('api/maintenance/', include('maintenance.api.urls')),
    path('api/users/', include('users.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# custom error views
handler404 = 'errors.views.error_404_view'
handler500 = 'errors.views.error_500_view'
handler403 = 'errors.views.error_403_view'