from django.conf.urls import patterns, url
from .views import books_view, books_serial_view, suma_view

urlpatterns = patterns('',
    url(r'^books/(?P<author>[\w\-]+)/', books_view, name='books_view'),
    url(r'^serial/', books_serial_view, name='books_serial'),
    url(r'^suma/', suma_view, name='suma_view'),
    
)
