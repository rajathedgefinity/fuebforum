# Generated by Django 2.2 on 2020-05-26 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0008_user_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='allthread',
            name='solved',
            field=models.BooleanField(default=False),
        ),
    ]