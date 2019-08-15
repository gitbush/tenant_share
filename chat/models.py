from django.db import models
from django.utils import timezone
from users.models import *
from maintenance.models import *

class ChatMessage(models.Model):
    """
    Model for a chat message
    """
    maint_request = models.ForeignKey(MaintRequest, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    message = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message
