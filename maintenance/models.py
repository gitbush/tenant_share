from django.db import models
from django.contrib.auth.models import User

# rental model for instances of rental properties
class Rental(models.Model):
    address = models.CharField(max_length=30)
    postcode = models.CharField(max_length=6)
    city = models.CharField(max_length=15)
    no_of_tenants = models.IntegerField()
    landlord = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.address

# maintenance request 
class MaintRequest(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    priority = models.CharField(max_length=20, default='low')
    status = models.CharField(max_length=20, default='new')
    date_occurred = models.DateField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    property_ref = models.ForeignKey(Rental, null=True, on_delete=models.SET_NULL ) 

    def __str__(self):
        return self.title



