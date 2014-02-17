from django.db import models
from django.contrib.auth.models import User as DjangoUser


class User(models.Model):
    user = models.CharField(max_length=100)
    auth_user = models.ForeignKey(DjangoUser)
    password = models.CharField(max_length=200)
