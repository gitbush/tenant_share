from django.db import models
from django.contrib.auth.models import User

class Maint_request(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    priority = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    date_occurred = models.DateField()
    image = models.ImageField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
