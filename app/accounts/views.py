import json
import urllib2

from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from accounts.forms import LoginForm
from accounts.models import User as Uuser

from entries.views import Init
from redmine import Redmine




class LoginView(TemplateView):
    template_name = "accounts/login.html"

    def get_context_data(request, *args, **kwargs):
        return {'form': LoginForm,
                'test': "test"}

class SignInView(View):
    def usernameexists(self, user, password):
        test = Redmine('http://pm.sophilabs.com/', username = user, password = password)

        try:
            test.projects['test']
        except urllib2.HTTPError:
            return False
        except KeyError:
            return True
        return True



    def post(self, request, *args, **kwargs):
        self.user_session = None
        self.usdj = None
        print dict(request.POST)
        self.res = json.dumps(request.POST)
        self.user = self.res.split(',')[2]
        self.user = self.user.replace('}', '')
        self.user = self.user.replace('"user": "', '')
        self.user = self.user.replace('"', '')
        self.user = self.user.replace(' ', '')
        self.password = self.res.split(',')[1]
        self.password = self.password.replace('}', '')
        self.password = self.password.replace('"password": "', '')
        self.password = self.password.replace('"', '')
        self.password = self.password.replace(' ', '')
        #self.entry_to_db = Entry(date = self.ConvertDate(self.fecha),
         #                        entry=self.content,
          #                       user_id=1)#test
        #self.entry_to_db.save()
        """if self.UserNameExists(self.user, self.password) is True:
            self.user_session = '%s' % self.user
        else:
            pass"""
        #self.Signinf(request)
        return self.Signinf(request)


    def Signinf(self, request):
        usera = None
        var = {}
        if self.usernameexists(self.user, self.password):
            usera = authenticate(username=self.user, password=self.password)
            if usera is None:
                self.usdj = User.objects.create_user(self.user, '', self.password)
                self.usdj.save()
                test = Uuser.objects.create(auth_user=self.usdj, user=self.user, password=self.password)
                test.save()
                var = {'login': 'wrong/registered', 'user': self.user}
            else:
                if usera.is_active:
                    login(request, usera)
                    #vamos a entries!!
                    var = {'login': 'successful', 'user': self.user}
                    Init.log_ok = usera

        else:
            var = {'login': 'wrong', 'user': self.user}

        return HttpResponse(json.dumps(var), content_type="application/json")

class LogOut(TemplateView):
    def get(self, request):
        logout(request)
        return super(LogOut, self).get(request)
    template_name = 'accounts/logout.html'