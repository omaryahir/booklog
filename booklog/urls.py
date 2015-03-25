from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'booklog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^listbooks/', 'books.views.listbooks_view', name='listbooks_view'),
)

if settings.DEBUG:
    # url static files
    #urlpatterns += patterns('django.contrib.staticfiles.views',
    #               url(r'^static/(P<path>.*)$', 'serve'),)
    urlpatterns += staticfiles_urlpatterns() 
    # url uploaded media
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 

   

