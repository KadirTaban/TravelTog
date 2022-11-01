import re
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_create', )

    def __str__(self):
        return self.title