# Generated by Django 2.2 on 2020-07-30 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_park_app', '0007_auto_20200730_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
