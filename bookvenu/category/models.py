from __future__ import unicode_literals


from django.db import models


class Category(models.Model):
    name = models.CharField(null=True, max_length=20)
    def __unicode__(self):
        return self.name