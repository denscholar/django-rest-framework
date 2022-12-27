from .models import Post
from rest_framework import serializers


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Post
        fields = ['title', 'content', 'created']