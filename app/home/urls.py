from django.conf.urls import patterns, url
from views import HomeView


urlpatterns = patterns('',
	 url(r'^$', HomeView.as_view()),
     #url(r'^login_request/$', SignInView.as_view()),
     #url(r'^logout/$', LogOut.as_view(), name='logout')
                       )
