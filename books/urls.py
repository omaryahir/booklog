from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import *

urlpatterns = patterns('',

    url(r'^books/(?P<author>[\w\-]+)/', books_view, name='books_view'),
    url(r'^serial/', books_serial_view, name='books_serial'),
    url(r'^suma/', suma_view, name='suma_view'),
    url(r'^create_book', book_create_view, name='create_book'),
    url(r'^edit_book/(?P<id_book>[0-9]+)', book_edit_view, name='edit_book'),

    url(r'^demo2/$', MyMostBasicView.as_view(), name='demo2'),
    url(r'^session/$', CreateSessionView.as_view(), name='session'),


    url(r'^contact/$', ContactView.as_view(), name="contact"),
    url(r'^contact/thank_you/$', TemplateView.as_view(template_name="thank_you.html"), name="thank_you"),

    url(r'^template_tag/$', TemplateTestView.as_view(), name="template_tag"),
    url(r'^filter/$', FilterTestView.as_view(), name="filter"),

)
