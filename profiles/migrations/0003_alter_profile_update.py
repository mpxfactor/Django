# Generated by Django 4.1.7 on 2023-03-05 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_created_alter_profile_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
