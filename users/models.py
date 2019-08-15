from django.db import models
from django.contrib.auth.models import User
from maintenance.models import Rental, MaintRequest
from PIL import Image

# extend django user model and add custom fields
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #creates relationship to user model

    # custom fields
    rental = models.ForeignKey(Rental, null=True, on_delete=models.SET_NULL)
    register_as = models.CharField(max_length=10, null=True)
    profile_image = models.ImageField(default='users/default_profile.jpg', upload_to='users')

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
    


