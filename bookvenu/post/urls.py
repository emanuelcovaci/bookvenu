from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create-post/', views.create_post, name='carete_post'),
    url(r'^post-name/', views.post, name='post'),
]
