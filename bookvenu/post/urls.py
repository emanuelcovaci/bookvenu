from django.conf.urls import url,include
from .views import *
from . import views

urlpatterns = [
    url(r'^create-post/', create_post, name='post-create'),
    url(r'^post/(?P<slug>[-\w]+)/$', get_post, name='post-get'),
    url(r'^post/(?P<slug>[\w-]+)/like/$', EventLike.as_view(), name='like-toggle'),
    url(r'^post/(?P<slug>[\w-]+)/delete/$', delete_post, name='delete-post'),
    url(r'^delete-comment/(?P<id>[\w-]+)/$' ,delete_comment, name='delete-comment'),
    url(r'^like-comment/(?P<id>[\w-]+)/$' ,CommentLike.as_view(), name='comm-toggle'),
    url(r'^edit/(?P<slug>[-\w]+)/', views.edit, name='edit'),
]