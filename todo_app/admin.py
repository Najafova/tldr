from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("category_name",)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title",)