from django.urls import path
from .views import *

urlpatterns = [
    # path('home_page/', post_request, name='home_page' ),
    # path('home_page/', CreateListApiView.as_view(), name='home_page' ),
    path('posts_list/', CreateListApiView.as_view(), name='posts_list'),
    path('<int:pk>', PostDetailUpdateDeleteView.as_view(), name='PostDetailUpdateDeleteView' ),
    # path('update/<int:id>/', update_post, name='update_post' ),
    # path('delete/<int:id>/', delete_post, name='delete_post' ),
]
