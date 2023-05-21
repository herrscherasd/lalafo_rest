from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAdminUser

from apps.categories.serializer import CategorySerializer
from apps.categories.models import Category

# Create your views here.
class CategoryAPIViewSet(GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            return (IsAdminUser(), )
        return (AllowAny(), )