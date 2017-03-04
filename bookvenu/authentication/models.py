from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User,primary_key = True)
    phonenumber = models.CharField(max_length = 10)

    BUCURESTI = 'BC'
    TIMISOARA = 'TM'

    CITY_CHOICES = (
        (BUCURESTI, 'Bucuresti'),
        (TIMISOARA, 'Timisoara'),
    )

    city_choices = models.CharField(max_length=10 , choices= CITY_CHOICES , default=BUCURESTI)
