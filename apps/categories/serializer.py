from rest_framework import serializers

from apps.categories.models import Category
from apps.posts.serializer import PostSerializer


class CategorySerializer(serializers.ModelSerializer):
    category_posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'title', 'category_posts')

