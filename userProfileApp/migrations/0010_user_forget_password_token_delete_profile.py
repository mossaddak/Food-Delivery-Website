# Generated by Django 4.1.3 on 2022-11-19 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfileApp', '0009_remove_user_forget_password_token_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='forget_password_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
