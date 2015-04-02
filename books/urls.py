from django.conf.urls import patterns, url
from .views import books_view, books_serial_view, suma_view, book_create_view

urlpatterns = patterns('',
    url(r'^books/(?P<author>[\w\-]+)/', books_view, name='books_view'),
    url(r'^serial/', books_serial_view, name='books_serial'),
    url(r'^suma/', suma_view, name='suma_view'),
    url(r'^create_book', book_create_view, name='create_book'),
    
)
