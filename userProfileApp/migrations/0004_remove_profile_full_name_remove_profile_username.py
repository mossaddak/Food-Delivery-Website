# Generated by Django 4.1.3 on 2022-11-16 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfileApp', '0003_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]
