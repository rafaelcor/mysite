from django.conf.urls import patterns, include, url

from django.contrib import admin

#from admin.views.
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('home.urls', namespace='home')),
    url(r'^about_me/', include('about_me.urls', namespace='aboutme')),
    url(r'^contact/', include('contact.urls', namespace='contact')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/', include('admin.urls', namespace='admin')),
)
