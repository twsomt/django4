#-*- coding: utf-8 -*-

from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    slug = models.SlugField()
    #template_name = ''

    def __str__(self):
        return str(self.title)
        