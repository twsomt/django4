from django.contrib import admin
from main_site.models import Articles

# Register your models here.

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content')