from django.db import models


class Entry(models.Model):

    STATUS_PENDING = 'P'
    STATUS_REGISTERED = 'R'
    STATUS = (
        (STATUS_PENDING, 'Pending',),
        (STATUS_REGISTERED, 'Registered',)
    )

    user = models.ForeignKey('accounts.User')
    status = models.CharField(max_length=1, choices=STATUS, default=STATUS_REGISTERED)
    date = models.DateField()
    entry = models.TextField()

    class Meta():
        unique_together = ('user', 'date',)
