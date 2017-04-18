from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create-post/', views.create_post, name='carete_post'),
    url(r'^post/(?P<slug>[^\.]+)/$', views.post, name='post'),
    url(r'^post/(?P<name>[a-zA-Z0-9]+)/', views.get_post, name='post-search'),
]
