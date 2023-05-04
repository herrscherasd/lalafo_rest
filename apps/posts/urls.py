from django.urls import path

from apps.posts.views import PostAPIView, PostCreateAPIView, PostUpdateAPIView, PostDestroyAPIView

urlpatterns = [
    path('posts/', PostAPIView.as_view(), name = 'api_posts'),
    path('posts/create/', PostCreateAPIView.as_view(), name = 'api_posts_create'),
    path('posts/update/<int:pk>/', PostUpdateAPIView.as_view(), name = 'api_posts_update'),
    path('posts/destroy/<int:pk>/', PostDestroyAPIView.as_view(), name = 'api_posts_destroy'),
]