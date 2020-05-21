from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    mobile = models.CharField(max_length=255, default="0000000000")
    facebook = models.CharField(max_length=255, blank=True)

class allthreads(models.Model):
    category = models.CharField(max_length=255,blank=True)
    product = models.CharField(max_length=255,blank=True)
    topic = models.CharField(max_length=255,blank=True)
    content = models.CharField(max_length=500,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    replies = models.IntegerField(default=0,blank=True)
    dateandtime = models.DateTimeField(auto_now=True,blank=True)
