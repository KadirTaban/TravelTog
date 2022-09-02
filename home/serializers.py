from dataclasses import field
import imp
from rest_framework import serializers
from .models import Journey


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields=['id','title','username','description','location','created_date','image','highlighted_image']
        