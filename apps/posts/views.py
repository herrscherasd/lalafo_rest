
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.posts.models import Post, FavoritePost
from apps.posts.serializer import PostSerializer, FavoritePostSerializer, PostDetailSerializer
from apps.posts.permission import PostPermission

# Create your views here.
class PostAPIViewSet(GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_permissions(self):
        if self.action in ('create', ):
            return(IsAuthenticated(), )
        if self.action in ('update', 'partial_update', 'destroy', ):
            return (IsAuthenticated(), PostPermission(), )
        return (AllowAny(), )
    
    def get_serializer_class(self):
        if self.action in ('retrieve', ):
            return PostDetailSerializer
        return PostSerializer


class FavoritePosAPIViewSet(GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin):
    queryset = FavoritePost.objects.all()
    serializer_class = FavoritePostSerializer

    def get_permissions(self):
        if self.action in ('destroy',):
            return (PostPermission(), )
        return (AllowAny(), )
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)