# Generated by Django 3.0.5 on 2020-04-13 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200412_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
