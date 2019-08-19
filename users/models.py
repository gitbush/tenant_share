from django.db import models
from django.contrib.auth.models import User
from maintenance.models import Rental, MaintRequest
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from PIL import Image

class Profile(models.Model):
    """
    Extend django user model and add custom fields
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE) #creates relationship to user model

    # custom fields
    rental = models.ForeignKey(Rental, null=True, on_delete=models.SET_NULL)
    register_as = models.CharField(max_length=10, null=True)

    # resize image on upload with django-imagekit
    profile_image = ProcessedImageField(upload_to='users',
                                           processors=[ResizeToFill(300, 300)],
                                           format='JPEG',
                                           options={'quality': 60})

    def __str__(self):
        return f'{self.user.username} Profile'

    #  resize uploaded profile img
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.profile_image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.profile_image.path)
    


