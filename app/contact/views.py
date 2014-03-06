import json
import urllib2

from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail

class Contact(TemplateView):
    template_name = "contact/contact.html"


class SendEmail(View):

    def post(self, request, *args, **kwargs):
        message = 0
        try:
            send_mail(request.POST['subject'],
                      "From:\n%s\n%s" % (request.POST['e-mail'], request.POST['message']),
                      request.POST['e-mail'],
                      ['rafael.cordano@gmail.com'], fail_silently=False)
            message = 'Yes'
        except:
            message = 'No'

        return HttpResponse(message)

