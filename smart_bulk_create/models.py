"""
    Created by tareq on 9/4/18
"""
from django.db import models

__author__ = "Tareq"

class MyModel(models.Model):
    name = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return self.name
