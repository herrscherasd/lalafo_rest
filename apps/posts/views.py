
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.posts.models import Post
from apps.posts.serializer import PostSerializer

# Create your views here.
class PostAPIViewSet(GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

