from django.conf.urls import url,include
from .views import *
from . import views

urlpatterns = [
    url(r'^contact/$', views.contact, name='contact'),
]