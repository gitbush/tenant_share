from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from utils.functions import resize_image

# rental model for instances of rental properties
class Rental(models.Model):
    address = models.CharField(max_length=30)
    postcode = models.CharField(max_length=8)
    city = models.CharField(max_length=15)
    no_of_tenants = models.IntegerField()
    image = models.ImageField(default='maintenance/no_image.jpg', upload_to='maintenance')
    landlord = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.address

    def save(self, *args, **kwargs):
        resize_image(self, Rental, self.image, 300)


# maintenance request 
class MaintRequest(models.Model):

    STATUS_CHOICES = [('new', 'New'), 
                      ('in-progress', 'In Progress'), 
                      ('awaiting-payment', 'Awaiting Payment'), 
                      ('resolved', 'Resolved')]
                      

    PRIORITY_CHOICES = [('low', 'Low'),
                        ('med', 'Med'),
                        ('high', 'High')]

    PAID_BY_CHOICES = [('tenant', 'Tenant'),
                       ('landlord', 'Landlord')]
                        

    property_ref = models.ForeignKey(Rental, null=True, on_delete=models.SET_NULL ) 
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=40)
    details = models.TextField()
    image = models.ImageField(default='maintenance/no_image.jpg', upload_to='maintenance')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, default='new', choices=STATUS_CHOICES)
    date_raised = models.DateTimeField(default=timezone.now)
    cost = models.IntegerField(null=True)
    paid_by = models.CharField(max_length=20, null=True, choices=PAID_BY_CHOICES)
    invoice_pdf = models.FileField(null=True, upload_to='maintenance')
    

    def __str__(self):
        return f"#{self.id}  {self.title} "

    def save(self, *args, **kwargs):
        resize_image(self, MaintRequest, self.image, 300)



