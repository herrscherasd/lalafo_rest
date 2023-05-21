from django.contrib import admin
from apps.posts.models import Post, FavoritePost

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'category', 'is_active']
    list_per_page = 20

@admin.register(FavoritePost)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'post']
    list_per_page = 20