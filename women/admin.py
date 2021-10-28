from django.contrib import admin
from .models import *


class WomenAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_create", "photo", "is_published")
    list_display_links = ("id", "title",)
    list_filter = ("is_published", "time_create",)
    search_fields = ("id", "title", "time_create",)
    list_editable = ("is_published",)
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_display_links = ("id", "name",)
    list_filter = ("id", "name",)
    search_fields = ("id", "name",)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)