# Generated by Django 3.1.5 on 2021-01-20 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationApp', '0013_auto_20210120_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.CharField(default='0000-00-00', max_length=12, null=True),
        ),
    ]
