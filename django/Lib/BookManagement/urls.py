
from django.conf.urls import url
from .views import first_book, first_book_h3, third

urlpatterns = [
 url(r'^fir/$', first_book),
  url(r'^firh3/$', first_book_h3),
  url(r'^thi/(?P<id>\d+)/$', third)
]
