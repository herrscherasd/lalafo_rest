from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена'
    )
    image = models.ImageField(
        upload_to='post_images/',
        verbose_name='Фотография'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"