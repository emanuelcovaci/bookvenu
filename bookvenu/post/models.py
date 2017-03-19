from __future__ import unicode_literals

from django.db import models

class EventModel(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length = 100)
    nrlocuri = models.CharField(max_length=15)
    date = models.CharField(max_length=15)
    price = models.CharField(max_length=15)
    phonenumber = models.CharField(max_length=10)
    details = models.CharField(max_length=1000)
    category = models.CharField(max_length=100)