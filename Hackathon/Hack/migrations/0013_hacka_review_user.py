# Generated by Django 4.1.7 on 2023-06-27 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hack', '0012_remove_user_registered_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='hacka',
            name='review_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Hack.user'),
            preserve_default=False,
        ),
    ]
