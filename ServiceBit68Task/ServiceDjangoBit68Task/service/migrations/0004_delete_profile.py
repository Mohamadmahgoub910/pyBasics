# Generated by Django 4.0.1 on 2022-01-13 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]