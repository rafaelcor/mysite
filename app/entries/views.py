import urllib2
import json
from redmine import Redmine
#from django.shortcuts import render_to_response
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
#from django.forms import ModelForm
from django.contrib.auth.views import redirect_to_login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.conf import settings
#from django import forms
from entries.forms import RegristryForm
from entries.models import Entry
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.utils.encoding import force_text
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from accounts.models import User as UserM


class AccessMixin(object):
    """
    'Abstract' mixin that gives access mixins the same customizable
    functionality.
    """
    login_url = None
    raise_exception = False  # Default whether to raise an exception to none
    redirect_field_name = REDIRECT_FIELD_NAME  # Set by django.contrib.auth

    def get_login_url(self):
        """
        Override this method to customize the login_url.
        """
        login_url = self.login_url or settings.LOGIN_URL
        if not login_url:
            raise ImproperlyConfigured(
                "Define %(cls)s.login_url or settings.LOGIN_URL or override "
                "%(cls)s.get_login_url()." % {"cls": self.__class__.__name__})

        return force_text(login_url)

    def get_redirect_field_name(self):
        """
        Override this method to customize the redirect_field_name.
        """
        if self.redirect_field_name is None:
            raise ImproperlyConfigured(
                "%(cls)s is missing the "
                "redirect_field_name. Define %(cls)s.redirect_field_name or "
                "override %(cls)s.get_redirect_field_name()." % {
                "cls": self.__class__.__name__})

        return self.redirect_field_name

class CsrfExemptMixin(object):
    """
    Exempts the view from CSRF requirements.

    NOTE:
        This should be the left-most mixin of a view.
    """

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        print "cs called"
        return super(CsrfExemptMixin, self).dispatch(*args, **kwargs)

class LoginRequiredMixin(AccessMixin):
    """
    View mixin which verifies that the user is authenticated.

    NOTE:
        This should be the left-most mixin of a view, except when
        combined with CsrfExemptMixin - which in that case should
        be the left-most mixin.
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            if self.raise_exception:
                raise PermissionDenied  # return a forbidden response
            else:
                return redirect_to_login(request.get_full_path(),
                                         self.get_login_url(),
                                         self.get_redirect_field_name())
        print "lr called"
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class Init(TemplateView, CsrfExemptMixin, LoginRequiredMixin):
    log_ok = None
    template_name = "entries/registry.html"
    atest = RegristryForm()



    def get_context_data(self):
        return {
                'test': "test"}


class Test(View):
    def ConvertDate(self, conv):
        months = ['Jan', 'Feb', 'Mar' ,'Apr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dec']
        conv = conv.replace(', ', ' ')
        lstring = conv.split(' ')
        lstring[0] = months.index(lstring[0])+1
        if lstring[0] < 10:
                lstring[0] = "0%s" % lstring[0]
        lstring = "%s-%s-%s" % (lstring[2], lstring[0], lstring[1])
        print lstring
        return lstring

    """def post(self, request, *args, **kwargs):
        print dict(request.POST)
        #self.entry_to_db = Entry(date = self.ConvertDate(json.dumps(dict(request.POST)['date'])),
         #                        entry=json.dumps(dict(request.POST)['content']))
        self.res = json.dumps(request.POST)
        self.fecha = self.res[10:22]
        self.content = self.res.replace(self.res[0:24], '')
        self.content = self.content.replace('}', '')
        self.content = self.content.split(',')[0]
        self.content = self.content.replace('"content": ', '')
        self.content = self.content.replace('"', '')
        self.entry_to_db = Entry(date = self.ConvertDate(self.fecha),
                                 entry=self.content,
                                 user_id=1)#test
        self.entry_to_db.save()
        return HttpResponse(self.content)
    """
    def get(self, request, *args, **kwargs):
        #print dict(request.GET)
        user = UserM.objects.filter(auth_user=self.request.user)[0]
        redmine_connect = Redmine('http://pm.sophilabs.com', username=user.user, password=user.password)

        content = [[], [], []]#1 proj 2 issue 3 actiity
        for project in redmine_connect.projects:
            content[0].append('@%s' % project.name)
        for project in redmine_connect.projects:
            try:
                for issue in project.issues:
                    content[1].append('#%s' % issue.id)
                    print issue[1]
            except:
                pass
        for activity in redmine_connect.time_entry_activities:
            #if '*' in activity:
                #activity.replace('*', '')
            content[2].append('$%s' % activity)
        return HttpResponse(json.dumps(content))


class ChartView(TemplateView):
    template_name = "entries/check.html"
    #def get(self, request, year, month, day):
        #YYYY-MM-DD format
        #return HttpResponse(Entry.objects.filter(date='%s-%s-%s' % (year, month, day)))