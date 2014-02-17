from django.conf.urls import patterns, url
from views import LoginView
from views import SignInView
from views import LogOut


urlpatterns = patterns('',
	 url(r'^$', LoginView.as_view()),
     url(r'^login_request/$', SignInView.as_view()),
     url(r'^logout/$', LogOut.as_view(), name='logout')
                       )
