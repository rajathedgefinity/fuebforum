# Generated by Django 2.2 on 2020-05-21 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allthreads',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='allthreads',
            name='shares',
            field=models.IntegerField(default=0),
        ),
    ]