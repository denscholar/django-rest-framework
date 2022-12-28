from .models import Post
from rest_framework import serializers


class PostModelSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    class Meta:
        model =  Post
        fields = ['id', 'title', 'content', 'created']