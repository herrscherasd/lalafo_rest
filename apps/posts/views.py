from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from apps.posts.models import Post
from apps.posts.serializer import PostSerializer

# Create your views here.
class PostAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDestroyAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer