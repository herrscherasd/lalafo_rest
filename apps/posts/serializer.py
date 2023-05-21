from rest_framework import serializers
from apps.posts.models import Post, FavoritePost

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description' , 'price', 'image', 'is_active', 'created', 'user', 'category')

class FavoritePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritePost
        fields = ('id', 'user', 'post')

class PostDetailSerializer(serializers.ModelSerializer):
    post_favorite_users = FavoritePostSerializer(many=True, read_only=True)
    favorite_users_count = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'description' , 'price', 'image', 'is_active', 'created', 'user', 'category', 'post_favorite_users', 'favorite_users_count')
        
    def get_favorite_users_count(self, obj):
        return obj.post_favorite_users.all().count()
    