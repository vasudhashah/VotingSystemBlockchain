# Generated by Django 3.1.5 on 2021-01-24 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationApp', '0019_auto_20210123_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
        migrations.AddField(
            model_name='user',
            name='is_ec_officer',
            field=models.BooleanField(default=False),
        ),
    ]
