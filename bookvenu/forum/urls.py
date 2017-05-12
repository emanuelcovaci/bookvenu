from django.conf.urls import url,include
from .views import *

urlpatterns = [
    url(r'^forum/$', forum_home, name='forum-home'),
    url(r'^forum/(?P<slug>[\w-]+)/$', forum_thread, name='forum-thread'),
    url(r'^forum/(?P<slug>[\w-]+)/delete-thread/$', thread_delete, name='thread-delete'),
    url(r'^forum/(?P<id>[\w-]+)/delete-comment/$', threadcom_delete, name='threadcom-delete'),
    url(r'^thread-comment/(?P<id>[\w-]+)/like/$', ThreadcomLike.as_view(), name='thcom-like'),
    url(r'^forum/(?P<slug>[\w-]+)/like/$', ThreadLike.as_view(), name='thread-like'),
]