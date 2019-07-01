from django.db import models
from django.contrib.auth.models import User

# image model for images of maintenance requests 
class MaintRequestImage(models.Model):
    image = models.ImageField(default='mantenance/no_image.jpg', upload_to='maintenance')

    def __str__(self):
        return self.image.url

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
    property_ref = models.ForeignKey(Rental, null=True, on_delete=models.SET_NULL ) 
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    image = models.ForeignKey(MaintRequestImage, null=True, on_delete=models.SET_NULL )
    title = models.CharField(max_length=200)
    details = models.TextField()
    priority = models.CharField(max_length=20, default='low')
    status = models.CharField(max_length=20, default='new')
    date_occurred = models.DateField()
    

    def __str__(self):
        return self.title



