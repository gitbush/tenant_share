from django.db import models
from django.utils import timezone
from maintenance.models import MaintRequest, User

# maint request payments model
class Payment(models.Model):
    """
    User Payment model for paying for maintenance requests
    """
    maint_request = models.ForeignKey(MaintRequest, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField()
    payment_date = models.DateTimeField(default=timezone.now)
    is_paid = models.BooleanField(default=False)
    payment_token = models.CharField(max_length=120, null=True)

    # assign current user to payment on create
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return self.maint_request.title
