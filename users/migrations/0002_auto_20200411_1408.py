# Generated by Django 3.0.5 on 2020-04-11 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='personalurl',
            new_name='site_url',
        ),
    ]
