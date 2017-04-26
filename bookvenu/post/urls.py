from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create-post/$', views.create_post, name='carete_post'),
    url(r'^post/(?P<slug>[-\w]+)/', views.post, name='post'),
    url(r'^like/$', views.like, name='like'),
    url(r'^edit/(?P<slug>[-\w]+)/', views.edit, name='edit'),
]
