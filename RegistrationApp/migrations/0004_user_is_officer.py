# Generated by Django 3.1.5 on 2021-01-19 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationApp', '0003_auto_20210119_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_officer',
            field=models.BooleanField(default=False),
        ),
    ]
