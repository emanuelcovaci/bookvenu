from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
def upload_location(instance, filename):
    return "%s/%s" % (instance.slug, filename)

class RequestModel(models.Model):
    autor = models.ForeignKey(to=User, related_name='requests',
                               null=True, blank=True)
    city = models.CharField(max_length = 100)
    nrlocuri = models.CharField(max_length=15)
    date = models.CharField(max_length=15)
    finaldate = models.CharField(max_length=15)
    price = models.CharField(max_length=15)
    phonenumber = models.CharField(max_length=10)
    details = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)

    def get_delete_url(self):
        return reverse("request:delete-request", kwargs={"slug": self.slug})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.city)
    if new_slug is not None:
        slug = new_slug
    qs =RequestModel.objects.filter(slug=slug).ordered_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.city)
    exists = RequestModel.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" % (slug, instance.id)
    instance.slug = slug



pre_save.connect(pre_save_post_receiver, sender=RequestModel)