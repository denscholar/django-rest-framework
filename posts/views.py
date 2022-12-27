from django.shortcuts import render
# from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from .models import Post
from .serializers import PostModelSerializer
from django.shortcuts import get_object_or_404


# list of post
class CreateListApiView(APIView):
    serializer_class = PostModelSerializer
    def get(self, request:Request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = self.serializer_class(instance=posts, many=True)

        response = {
            "message": "all post",
            "data": serializer.data
        }

        return Response(response, status=status.HTTP_201_CREATED)
        

    def post(self, request:Request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "post created",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)



class PostDetailUpdateDeleteView(APIView):
    serializer_class = PostModelSerializer

    def get(self, request:Request, id):
        post = get_object_or_404(Post, id=id)
        serializer = self.serializer_class(instance=post)

        response = {
            "message": "post retrived successfully",
            "data": serializer.data
        }

        return Response(response, status=status.HTTP_201_CREATED)
    
    def put(self, request:Request, id):
        post = get_object_or_404(Post, id=id)
        data = request.data
        serializer = self.serializer_class(instance=post, data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "post updated successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request:Request, id):
        post = get_object_or_404(Post, id=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


