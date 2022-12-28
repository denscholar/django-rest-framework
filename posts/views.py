from django.shortcuts import render
# from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView
from .models import Post
from .serializers import PostModelSerializer
from django.shortcuts import get_object_or_404


# list of post
class CreateListApiView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializer_class = PostModelSerializer
    queryset = Post.objects.all()

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostDetailUpdateDeleteView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = PostModelSerializer
    queryset = Post.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)