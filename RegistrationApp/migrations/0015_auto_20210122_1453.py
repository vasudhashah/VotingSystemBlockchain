# Generated by Django 3.1.5 on 2021-01-22 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationApp', '0014_auto_20210120_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='color',
            field=models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=6),
        ),
        migrations.AddField(
            model_name='user',
            name='pincode',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
