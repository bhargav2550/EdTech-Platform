# Generated by Django 4.1.7 on 2023-06-26 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hack', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hacka',
            name='BackGround_Image',
        ),
        migrations.RemoveField(
            model_name='hacka',
            name='Hackathon_Image',
        ),
    ]
