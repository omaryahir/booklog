from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'booklog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^listbooks/', 'books.views.listbooks_view', name='listbooks_view'),
    url(r'', include('books.urls')),
    url(r'^demo/$', TemplateView.as_view(template_name="template_base.html"), name="demo"),
)

if settings.DEBUG:
    # url static files
    urlpatterns += staticfiles_urlpatterns() 
    
    # url uploaded media
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 

   

