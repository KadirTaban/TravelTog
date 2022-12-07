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
    image = models.ImageField(upload_to='images/', default ='default.jpg', null=True)   
    image_2 = models.ImageField(upload_to='images/', default ='default.jpg', null=True) 
    image_3 = models.ImageField(upload_to='images/', default ='default.jpg', null=True)   
  
    class Meta:
        ordering = ('-date_create', )

    def comment_count(self):
        return self.comment_set.all().count()

    def comments(self):
        return self.comment_set.all()

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
       return self.content