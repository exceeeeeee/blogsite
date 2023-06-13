from django.contrib import admin
from .models import *


# Register your models here.


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'time_create', 'photo', 'is_published')
    list_display_links = ('id',)
    search_fields = ('title', 'content')
    list_editable = ['is_published', 'title']
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Women, WomenAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_editable = ['name', ]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
