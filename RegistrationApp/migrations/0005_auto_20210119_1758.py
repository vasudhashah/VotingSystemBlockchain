# Generated by Django 3.1.5 on 2021-01-19 12:28

import RegistrationApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationApp', '0004_user_is_officer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='aadhar_no',
            field=models.CharField(default='000000000000', max_length=100, validators=[RegistrationApp.models.aadhar_check]),
        ),
    ]
