import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Journey(models.Model):
    id=models.IntegerField(primary_key=True)
    username = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=55)
    created_date=models.DateField(datetime.datetime.now())
    image = models.ImageField(upload_to='images')
    highlighted_image = models.ImageField(upload_to='highlighted_images')




