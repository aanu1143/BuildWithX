from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    site_url = models.CharField(max_length=200, null=True, blank=True)
    bio = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True, blank=True)