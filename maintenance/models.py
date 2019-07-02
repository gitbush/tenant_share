from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# rental model for instances of rental properties
class Rental(models.Model):
    address = models.CharField(max_length=30)
    postcode = models.CharField(max_length=6)
    city = models.CharField(max_length=15)
    no_of_tenants = models.IntegerField()
    image = models.ImageField(default='mantenance/no_image.jpg', upload_to='maintenance')
    landlord = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.address

# maintenance request 
class MaintRequest(models.Model):

    STATUS_CHOICES = [(None, 'Status'),
                      ('new', 'New'), 
                      ('in-progress', 'In Progress'), 
                      ('awaiting-payment', 'Awaiting Payment'), 
                      ('resolved', 'Resolved')]

    PRIORITY_CHOICES = [('low', 'Low'),
                        ('med', 'Med'),
                        ('high', 'High')]
                        

    property_ref = models.ForeignKey(Rental, null=True, on_delete=models.SET_NULL ) 
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=40)
    details = models.TextField()
    image = models.ImageField(default='mantenance/no_image.jpg', upload_to='maintenance')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, default='new', choices=STATUS_CHOICES)
    date_raised = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.title



