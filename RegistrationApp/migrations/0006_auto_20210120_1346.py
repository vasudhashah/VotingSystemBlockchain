# Generated by Django 3.1.5 on 2021-01-20 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationApp', '0005_auto_20210119_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
