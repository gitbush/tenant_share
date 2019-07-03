from django.db import models
from django.utils import timezone
from users.models import *
from maintenance.models import *

# model for each message thread
class Thread(models.Model):
    rental = models.ForeignKey(Rental, null=True, on_delete=models.CASCADE)
    maint_request = models.ForeignKey(MaintRequest, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.maint_request.title

# model for message in each thread
class ChatMessage(models.Model):
    thread = models.ForeignKey(Thread, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    message = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message
