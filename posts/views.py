from django.shortcuts import render
# from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


posts = [
    {
        "id": 1,
        "title": "this is my first title",
        "content": "this is going to be a good learning"
    },
    {
        "id": 2,
        "title": "this is my second title",
        "content": "this is going to be a good learning two"
    },
    {
        "id": 3,
        "title": "this is my third title",
        "content": "this is going to be a good learning three"
    }
]


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
@api_view(http_method_names=['GET'])
def posts_list(request:Request):
    return Response(data=posts, status=status.HTTP_201_CREATED)

# post details
@api_view(http_method_names=['POST'])
def posts_detail(request:Request, id):
    post = posts[id] #get a single post by it's id

    if post:
        return Response(data=post, status=status.HTTP_201_CREATED)
    return Response(data={"error": "eror post not found"})
