from django.db import models
from django.utils import timezone
from maintenance.models import MaintRequest, User

# maint request payments model
class Payment(models.Model):
    maint_request = models.ForeignKey(MaintRequest, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField()
    payment_date = models.DateTimeField(default=timezone.now)
    is_paid = models.BooleanField(default=False)
    payment_token = models.CharField(max_length=120, null=True)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return self.maint_request.title
