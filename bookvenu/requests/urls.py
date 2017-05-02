from django.conf.urls import url,include
from .views import *
from . import views

urlpatterns = [
    url(r'^create-request/', create_request, name='request-create'),
    url(r'^request/(?P<slug>[\w-]+)/delete/$', delete_requests, name='delete-request'),
]