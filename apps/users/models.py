from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(
        max_length=100,
        verbose_name="Телефонный номер"
        )
    profile_image = models.ImageField(
        upload_to='profile_image/',
        verbose_name="Фотография профиля"
        )
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"