# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def first_book(request):
    return HttpResponse('<h1> This is first view in Book</h1>')

def first_book_h3(request):
    return HttpResponse('<h3> This is first view in Book with h3</h3>')

def third(request, **kwargs):
    return HttpResponse('<h1> You have sent %s as ID</h1>' %kwargs['id']) 