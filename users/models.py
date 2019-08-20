from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage as storage
from maintenance.models import Rental, MaintRequest
from PIL import Image, ImageOps
from utils.functions import upload_to, resize_image

# # have username in uploaded image path
# def upload_to(instance, filename):
#     return "users/%s/%s" % (instance.user.username.lower(), filename)

class Profile(models.Model):
    """
    Extend django user model and add custom fields
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE) #creates relationship to user model

    # custom fields
    rental = models.ForeignKey(Rental, null=True, on_delete=models.SET_NULL)
    register_as = models.CharField(max_length=10, null=True)

    profile_image = models.ImageField(default='users/default_profile.jpg', upload_to=upload_to)

    def __str__(self):
        return f'{self.user.username} Profile'

    # resize uploaded profile img
    def save(self, *args, **kwargs):
        resize_image(self, Profile, self.profile_image, 300)
     
    


