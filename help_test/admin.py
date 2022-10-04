from django.contrib import admin
from help_test.models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'tags')