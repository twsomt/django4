from django import urls
from django.urls import path
from django.urls.conf import re_path
from main_site.views import ArticlesListView

urlpatterns = [
    re_path(f'^$', ArticlesListView.as_view(), name='list')
] 