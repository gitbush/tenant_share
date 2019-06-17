from django.db import models
from django.contrib.auth.models import User
from maintenance.models import Rental, MaintRequest

# extend django user model and add custom fields
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #creates relationship to user model

    # custom fields
    register_as = models.CharField(max_length=10, null=True)
    rental = models.ForeignKey(Rental, null=True, on_delete=models.SET_NULL)
    requests = models.ForeignKey(MaintRequest, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.user.username} Profile'


    


