#-*- coding: utf-8 -*-

from unittest.util import _MAX_LENGTH
from xml.dom.minidom import CharacterData
from django.db import models
from django.forms import CharField

class Articles(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)