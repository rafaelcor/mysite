from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt

from views import Contact
from views import SendEmail


urlpatterns = patterns('',
	 url(r'^$', Contact.as_view()),
     url(r'^sendmail$', SendEmail.as_view())
     #url(r'^login_request/$', SignInView.as_view()),
     #url(r'^logout/$', LogOut.as_view(), name='logout')
                       )
