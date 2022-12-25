from django.urls import path
from .views import *

urlpatterns = [
    path('home_page', post_request, name='home_page' ),
]
