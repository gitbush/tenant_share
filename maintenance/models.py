from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.files.storage import default_storage as storage
from PIL import Image, ImageOps
from utils.functions import resize_image

# have address in uploaded image path
def upload_to(instance, filename):
    return "maintenance/%s/%s" % (instance.address.lower(), filename)


# rental model for instances of rental properties
class Rental(models.Model):
    address = models.CharField(max_length=30)
    postcode = models.CharField(max_length=8)
    city = models.CharField(max_length=15)
    no_of_tenants = models.IntegerField()
    image = models.ImageField(default='maintenance/no_image.jpg', upload_to=upload_to)
    landlord = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.address

     # TODO: DRY save method for resize images
    def save(self, *args, **kwargs):
        """
        - installed 'django-cleanup' to auto-remove old image.
        - installed 'pillow' to resize larger images.
        """
        super(Rental, self).save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image)
            size = 300
            thumb = (size, size)
            method = Image.ANTIALIAS
            center = (0.5, 0.5)
            extension = "png"
            # if greater than 300px on any side, then resize it to 300x300
            if img.height > size or img.width > size:
                img.thumbnail((size, size), method)
                center_img = ImageOps.fit(img, thumb, method, centering=center)
                temp = storage.open(self.image.name, "w")
                center_img.save(temp, extension)
                temp.close()
                super(Rental, self).save(*args, **kwargs) 


# maintenance request 
class MaintRequest(models.Model):

    STATUS_CHOICES = [('new', 'New'), 
                      ('in-progress', 'In Progress'), 
                      ('awaiting-payment', 'Awaiting Payment'), 
                      ('resolved', 'Resolved')]
                      

    PRIORITY_CHOICES = [('low', 'Low'),
                        ('med', 'Med'),
                        ('high', 'High')]

    PAID_BY_CHOICES = [('Tenant', 'Tenant'),
                       ('Landlord', 'Landlord')]
                        

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
    invoice_pdf = models.FileField(null=True, upload_to='maintenance', blank=True)
    

    def __str__(self):
        return f"#{self.id}  {self.title} "

    def save(self, *args, **kwargs):
        """
        - installed 'django-cleanup' to auto-remove old image.
        - installed 'pillow' to resize larger images.
        """
        super(MaintRequest, self).save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image)
            size = 300
            thumb = (size, size)
            method = Image.ANTIALIAS
            center = (0.5, 0.5)
            extension = "png"
            # if greater than 300px on any side, then resize it to 300x300
            if img.height > size or img.width > size:
                img.thumbnail((size, size), method)
                center_img = ImageOps.fit(img, thumb, method, centering=center)
                temp = storage.open(self.image.name, "w")
                center_img.save(temp, extension)
                temp.close()
                super(MaintRequest, self).save(*args, **kwargs) 




