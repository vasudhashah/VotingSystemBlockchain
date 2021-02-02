# Generated by Django 3.1.5 on 2021-01-20 08:35

import RegistrationApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationApp', '0008_auto_20210120_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='aadhar_no',
            field=models.CharField(max_length=100, unique=True, validators=[RegistrationApp.models.aadhar_check]),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='Super', max_length=100),
        ),
    ]
