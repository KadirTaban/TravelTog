from dataclasses import field
import imp
from rest_framework import serializers
from .models import Journey


class MyGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields=['id','title','username','description','location','created_date','image','highlighted_image']
    
class MainFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields=['id','title','username','description','location','created_date','image','highlighted_image']
        