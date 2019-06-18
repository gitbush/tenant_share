from django.contrib import admin
from maintenance.models import Rental, MaintRequest, MaintRequestImage

admin.site.register(Rental)
admin.site.register(MaintRequest)
admin.site.register(MaintRequestImage)

