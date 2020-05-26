import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

# Create your models here.
class User(AbstractUser):

    GENDER = (
        (None, _('Select Your Gender')),
        ('Male', _('Male')),
        ('Female', _('Female')),
    )

    cover = models.ImageField(upload_to='profileimages/', blank=True)
    mobile = models.CharField(max_length=255, default="0000000000")
    gender = models.CharField(max_length=7, choices=GENDER, blank=True)
    city = models.CharField(max_length=30, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    nationality = CountryField(null=True)
    dob = models.DateField(default=datetime.date.today)

class allthread(models.Model):
    thread_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255,blank=True)
    product = models.CharField(max_length=255,blank=True)
    topic = models.CharField(max_length=255,blank=True)
    content = models.CharField(max_length=500,blank=True)
    thread_by = models.ForeignKey(User, on_delete=models.CASCADE)
    replies = models.IntegerField(default=0,blank=True)
    thread_status = models.BooleanField(default=False)
    dateandtime = models.DateTimeField(auto_now=True,blank=True)
    solved = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
