from django.shortcuts import render
from django.http import HttpRequest, JsonResponse

def post_request(request=HttpRequest):
    response = {
        "message": "this is a simple api created"
    }
    return JsonResponse(data=response)
