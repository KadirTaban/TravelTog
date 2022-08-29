import datetime
from django.db import models

# Create your models here.


class Traveller(models.Model):
    travellers = models.CharField(max_length=200)

    def __str__(self):
        return self.travellers
    
class Journey(models.Model):
    id=models.IntegerField(primary_key=True)
    travellers= models.ManyToManyField(Traveller, blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=55)
    created_date=models.DateField(datetime.datetime.now())
    image = models.ImageField(upload_to='images')
    highlighted_image = models.ImageField(upload_to='highlighted_images')
