from django.conf.urls import patterns, url
from views import AboutMe


urlpatterns = patterns('',
	 url(r'^bio$', AboutMe.Bio.as_view()),
     url(r'^projs$', AboutMe.Projs.as_view()),
     #url(r'^login_request/$', SignInView.as_view()),
     #url(r'^logout/$', LogOut.as_view(), name='logout')
                       )
