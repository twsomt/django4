from enum import unique
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True)
    # tags = models.TextField(null=True)
    # tags = models.TextField(null=False)
    tags = models.TextField(blank=True)
    def __str__(self):

        return str(self.name)