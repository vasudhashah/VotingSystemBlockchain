# Generated by Django 3.1.5 on 2021-01-23 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationApp', '0016_auto_20210122_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
