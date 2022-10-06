from django.contrib import admin
from main_site.models import Articles


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content')