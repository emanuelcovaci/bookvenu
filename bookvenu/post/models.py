from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models
from category.models import Category
import uuid
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import pre_save

def upload_location(instance, filename):
    return "%s/%s" % (instance.slug, filename)

class EventModel(models.Model):
    author = models.ForeignKey(to=User, related_name='posts',
                               null=True, blank=True)
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length = 100)
    nrlocuri = models.CharField(max_length=15)
    date = models.CharField(max_length=15)
    site = models.CharField(max_length=50,default='')
    finaldate = models.CharField(max_length=15)
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
    slug = models.SlugField(unique=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes')

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("post:post-get", kwargs={"slug": self.slug})

    def get_like_url(self):
        return reverse("post:like-toggle", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse("post:delete-post", kwargs={"slug": self.slug})

    def get_reserve_url(self):
        return reverse("post:create-reserve", kwargs={"slug": self.slug})

    def people_going(self):
        qs = Reserve.objects.filter(post=self)
        total = 0
        for q in qs:
            total = total + int(q.nrlocuri)
        return total


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = EventModel.objects.filter(slug=slug).ordered_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.name)
    exists = EventModel.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" % (slug, instance.id)
    instance.slug = slug


pre_save.connect(pre_save_post_receiver, sender=EventModel)


class Comment(models.Model):
    post = models.ForeignKey(EventModel, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    parent = models.ForeignKey("self", blank=True, null=True)
    is_parent = models.BooleanField(default=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='comm_likes')

    class Meta:
        ordering = ['-date_created']

    def approved(self):
        self.save()

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.body

    def children(self):
        return Comment.objects.filter(parent=self)

    def get_like_url(self):
        return reverse("post:comm-toggle", kwargs={"id": self.id})

    def get_delete_comm(self):
        return reverse("post:delete-comment", kwargs={'id': self.id})


class Reserve(models.Model):
    user = models.ForeignKey(to=User, null=True, blank=True)
    post = models.ForeignKey(EventModel, null=True, blank=True)
    nrlocuri = models.CharField(max_length=15)

    def get_delete_url(self):
        return reverse("reserve:delete", kwargs={'id':self.id})