
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models
from category.models import Category
import uuid
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import pre_save

class Thread(models.Model):
    user = models.ForeignKey(to=User,related_name='threads')
    name = models.CharField(max_length = 100)
    body = models.CharField(max_length = 1000)
    data_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='thread_likes')

    def get_absolute_url(self):
        return reverse("forum:forum-thread", kwargs={'slug':self.slug})

    def get_like_url(self):
        return reverse("forum:thread-like", kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse("forum:thread-delete", kwargs={'slug':self.slug})

    def total_likes(self):
        return self.likes.count()

def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Thread.objects.filter(slug=slug).ordered_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.name)
    exists = Thread.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" % (slug, instance.id)
    instance.slug = slug


pre_save.connect(pre_save_post_receiver, sender=Thread)
class ThreadComment(models.Model):
    post = models.ForeignKey(Thread, related_name='comment')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey("self", blank=True, null=True)
    is_parent = models.BooleanField(default=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='t_comm_likes')

    def total_likes(self):
        return self.likes.count()

    def str(self):
        return self.body

    def children(self):
        return ThreadComment.objects.filter(parent=self)

    def get_like_url(self):
        return reverse("forum:thcom-like", kwargs={'id':self.id})

    def get_delete_url(self):
        return reverse("forum:threadcom-delete", kwargs={'id':self.id})