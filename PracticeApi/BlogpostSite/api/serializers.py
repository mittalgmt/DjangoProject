#create a class that will take this model and convert into Jason Compatible data

from rest_framework import serializers
from .models import*

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id","title","content","published_date"]
        