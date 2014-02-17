import json
import urllib2

from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class AboutMe():
    #template_name = "about_me/contact.html"

    class Bio(TemplateView):
        print
        template_name = "about_me/about_bio.html"

    class Projs(TemplateView):
        print
        template_name = "about_me/about_projs.html"
