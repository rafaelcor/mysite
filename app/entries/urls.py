from django.conf.urls import patterns, url
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.decorators import login_required
from views import Init, ChartView, Test

urlpatterns = patterns('',
                       url(r'^$', requires_csrf_token(login_required(Init.as_view()))),
                       url(r'^sendinfo$', Test.as_view()),
                       url(r'^check/(?P<year>\w{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', ChartView.as_view()),
)
