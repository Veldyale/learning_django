from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Women)

class PersonAdmin(admin.ModelAdmin):
    list_display = ("title", "time_create",)
    list_filter = ("title", "time_create",)

    search_fields = ("title", "time_create",)

@admin.register(Category)

class PersonAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)

    search_fields = ("name",)