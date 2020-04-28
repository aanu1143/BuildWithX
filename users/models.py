from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class CustomUser(AbstractUser):
    bio = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to= 'img/', height_field=None, width_field=None, max_length=100, null=True)
    
    def get_absolute_url(self):
        return reverse('profile_detail',args=[str(self.id)])
