from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models
from category.models import Category
import uuid

def upload_location(instance, filename):
    return "%s/%s" % (instance.slug, filename)

class EventModel(models.Model):
    author = models.ForeignKey(to=User, related_name='posts',
                               null=True, blank=True)
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length = 100)
    nrlocuri = models.CharField(max_length=15)
    date = models.CharField(max_length=15)
    price = models.CharField(max_length=15)
    phonenumber = models.CharField(max_length=10)
    details = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, null=True)
    image1 = models.ImageField(upload_to=upload_location,
                              null=True, blank=True)
    image2 = models.ImageField(upload_to=upload_location,
                           null=True, blank=True)
    image3 = models.ImageField(upload_to=upload_location,
                           null=True, blank=True)
    image4 = models.ImageField(upload_to=upload_location,
                           null=True, blank=True)
    slug = models.SlugField(default=uuid.uuid1, unique=True)

    def get_absolute_url(self):
        return reverse('event', args=[self.slug])