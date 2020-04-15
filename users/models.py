from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class CustomUser(AbstractUser):
    site_url = models.CharField(max_length=200, null=True)
    bio = models.CharField(max_length=50, null=True)
    dob = models.DateField(auto_now=False, null=True)
    contact_number = models.CharField(max_length=10, null=True)
    image = models.ImageField(upload_to= 'img/', height_field=None, width_field=None, max_length=100, null=True)
    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES,  null=True)

    def get_absolute_url(self):
          return reverse('profile_detail',args=[str(self.id)])
