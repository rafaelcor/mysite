import json
import urllib2

from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class Contact(TemplateView):
    template_name = "contact/contact.html"


class SendEmail(View):

    def post(self, request, *args, **kwargs):
        return HttpResponse(request.POST)

