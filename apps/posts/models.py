from django.db import models
from django.contrib.auth import get_user_model

from apps.categories.models import Category

User = get_user_model()


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='user_posts',
        verbose_name='Пользователи'
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True, null=True
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена',
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='post_images/',
        verbose_name='Фотография'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        related_name='category_posts',
        verbose_name='Категория',
        blank=True, null=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Статус поста'
    )



    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

class FavoritePost(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='user_favorites',
        verbose_name='Пользователь'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='post_favorite_users',
        verbose_name='Пост'
    )



    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = "Избранные"