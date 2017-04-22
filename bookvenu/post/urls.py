from django.conf.urls import url
from . import views
from .views import *

urlpatterns = [
    url(r'^create-post/$', views.create_post, name='carete_post'),
    url(r'^post/(?P<slug>[-\w]+)/', views.post, name='post'),
    url(r'^like/$', views.like, name='like'),
]
