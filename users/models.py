from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class CustomUser(AbstractUser):
    site_url = models.CharField(max_length=200, null=True, blank=True)
    bio = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to= 'img/', height_field=None, width_field=None, max_length=100, null=True, blank=True)

    def get_absolute_url(self):
          return reverse('profile_detail',args=[str(self.id)])