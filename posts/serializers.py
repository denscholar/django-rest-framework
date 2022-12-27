from .models import Post
from rest_framework import serializers


class PostModelSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    class Meta:
        model =  Post
        fields = ['title', 'content', 'created']