from django.contrib import admin

from apps.categories.models import Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title',]
    search_fields = ['title',]
    list_per_page = 20