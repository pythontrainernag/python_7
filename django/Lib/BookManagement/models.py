# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50)

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    book = models.ManyToManyField(Book)

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    website = models.CharField(max_length=50)
    books = models.ForeignKey(Book)
        
