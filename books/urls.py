from django.conf.urls import patterns, url


from .views import *

urlpatterns = patterns('',
    url(r'^books/(?P<author>[\w\-]+)/', books_view, name='books_view'),
    url(r'^serial/', books_serial_view, name='books_serial'),
    url(r'^suma/', suma_view, name='suma_view'),
    url(r'^create_book', book_create_view, name='create_book'),
    url(r'^edit_book/(?P<id_book>[0-9]+)', book_edit_view, name='edit_book'),

    url(r'^demo2/$', MyMostBasicView.as_view(), name='demo2'),
    url(r'^session/$', CreateSessionView.as_view(), name='session')

)
