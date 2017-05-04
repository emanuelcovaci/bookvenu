from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(to=User,blank = True,null = True)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)