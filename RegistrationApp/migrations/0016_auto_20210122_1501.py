# Generated by Django 3.1.5 on 2021-01-22 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationApp', '0015_auto_20210122_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='color',
        ),
        migrations.AddField(
            model_name='user',
            name='constituency',
            field=models.CharField(max_length=100, null=True),
        ),
    ]