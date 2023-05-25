from django.contrib import admin


from apps.telegram.models import TelegramUser
# Register your models here.
@admin.register(TelegramUser)
class TelegramUser(admin.ModelAdmin):
    list_display = ('id_user', 'username', 'created')
    search_fields = ('id_user', 'username', 'created')
    list_per_page = 20