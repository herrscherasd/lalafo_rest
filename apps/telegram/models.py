from django.db import models

# Create your models here.
class TelegramUser(models.Model):
    id_user = models.CharField(
        max_length=100,
        verbose_name='ID пользователя Telegram')
    username = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя",
        blank=True, null=True
    )
    first_name = models.CharField(
        max_length=255, 
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name='Фамилия',
        blank=True, null=True
    )
    chat_id = models.CharField(
        max_length=100,
        verbose_name='Чат ID'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата регистрации'
    )

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Пользователь Телеграм'
        verbose_name_plural = "Пользователи Телеграма"