from django.conf.urls import patterns, url
from .views import books_view

urlpatterns = patterns('',
    url(r'^books/(?P<author>[\w\-]+)/', books_view, name='books_view'),
)
