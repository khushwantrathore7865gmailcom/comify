# Generated by Django 3.2.4 on 2023-05-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_auto_20230509_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='service_profile/'),
        ),
    ]
