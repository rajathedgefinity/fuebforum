# Generated by Django 2.2 on 2020-05-25 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_auto_20200521_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cover',
            field=models.ImageField(blank=True, upload_to='profileimages/'),
        ),
    ]