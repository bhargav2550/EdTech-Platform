# Generated by Django 4.1.7 on 2023-06-27 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hack', '0011_alter_user_registered_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Registered_to',
        ),
    ]
