from django.views.generic import ListView, DetailView
from main_site.models import Articles


class ArticlesListView(ListView):
    model = Articles