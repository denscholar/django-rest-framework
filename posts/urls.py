from django.urls import path
from .views import *

urlpatterns = [
    path('home_page/', post_request, name='home_page' ),
    path('posts_list/', posts_list, name='posts_list' ),
    path('<int:id>', posts_detail, name='post_detail' ),
]
