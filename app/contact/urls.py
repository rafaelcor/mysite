from django.conf.urls import patterns, url
from views import Contact


urlpatterns = patterns('',
	 url(r'^$', Contact.as_view()),
     #url(r'^login_request/$', SignInView.as_view()),
     #url(r'^logout/$', LogOut.as_view(), name='logout')
                       )
