# Generated by Django 4.1.7 on 2023-03-05 05:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('website', models.URLField(blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
