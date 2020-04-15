from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse

types = (
    ('developer', 'Developer'),
    ('finder', 'Finder'),)


class Framework(models.Model):
    language = models.CharField(max_length=30)
    def __str__(self):
        return self.language

class Project(models.Model):
    project_name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    build_with = models.ManyToManyField('Framework')
    url = models.URLField(max_length=200, null=True)
    website_image = models.ImageField(upload_to= 'img/', height_field=None, width_field=None, max_length=100, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='profileuser', null=True)
    date = models.DateTimeField(auto_now_add=True)
    user_type = models.CharField(max_length=25,choices=types, null=True)


    def get_absolute_url(self):
        return reverse('profile_project', kwargs={'pk': self.pk})

    def __str__(self):
        return self.project_name
