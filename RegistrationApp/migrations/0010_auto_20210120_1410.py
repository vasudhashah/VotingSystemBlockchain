# Generated by Django 3.1.5 on 2021-01-20 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationApp', '0009_auto_20210120_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='full_name',
        ),
    ]