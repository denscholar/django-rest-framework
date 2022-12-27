from django.shortcuts import render
# from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostModelSerializer
from django.shortcuts import get_object_or_404


@api_view(http_method_names=['GET', 'POST'])
def post_request(request=Request):

    if request.method == 'POST':
        data = request.data
        response = {
            "message": data
        }
        return Response(data=response, status=status.HTTP_201_CREATED)
    response = {
        "message": "this is a simple api created using rest framework"
    }
    return Response(data=response, status=status.HTTP_200_OK)

# list of post


@api_view(http_method_names=['GET', 'POST'])
def posts_list(request: Request):
    posts = Post.objects.all()

    if request.method == 'POST':
        data = request.data
        serializer = PostModelSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "mesage": "post created successfully",
                "data": serializer.data,
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = PostModelSerializer(instance=posts, many=True)
    response = {
        "message": 'posts',
        "data": serializer.data
    }
    return Response(data=response, status=status.HTTP_201_CREATED)

# post details


@api_view(http_method_names=['GET'])
def posts_detail(request: Request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostModelSerializer(instance=post)
    response = {
        "message": "post detail created",
        "data": serializer.data
    }
    return Response(data=response, status=status.HTTP_201_CREATED)

@api_view(http_method_names=['PUT'])
def update_post(request: Request, id):
    post = get_object_or_404(Post, id=id)
    data = request.data
    serializer = PostModelSerializer(instance=post, data=data)
    if serializer.is_valid():
        serializer.save()

        response = {
            "message": "post detail created",
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['DELETE'])
def delete_post(request: Request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)