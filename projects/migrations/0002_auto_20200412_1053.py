# Generated by Django 3.0.5 on 2020-04-12 05:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profileuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='user_type',
            field=models.CharField(choices=[('developer', 'Developer'), ('finder', 'Finder')], max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='website_image',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
    ]
