# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import default

# Create your models here.



class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name+self.last_name

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    website = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=50)
    publisher = models.ForeignKey(Publisher, default=0)
    authors = models.ManyToManyField(Author)
    def __str__(self):
        return self.name
