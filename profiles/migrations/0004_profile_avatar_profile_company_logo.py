# Generated by Django 4.1.7 on 2023-03-10 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='images/avatar.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='company_logo',
            field=models.ImageField(default='images/no_photo.png', upload_to=''),
        ),
    ]
