from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import AllowAny

from apps.users.models import User
from apps.users.permission import UserPermission
from apps.users.serializer import UserSerializer, UserRegisterSerializer, UserDetailSerializer

# Create your views here.
class UsersAPIViewSet(GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action in ('create', ):
            return UserRegisterSerializer
        if self.action in ('retrieve', ):
            return UserDetailSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (UserPermission(), )
        return (AllowAny(), )