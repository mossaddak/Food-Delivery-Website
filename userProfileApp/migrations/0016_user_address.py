# Generated by Django 4.1.3 on 2022-11-22 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfileApp', '0015_remove_foodmenu_category_delete_foodcategories_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=264, null=True),
        ),
    ]
