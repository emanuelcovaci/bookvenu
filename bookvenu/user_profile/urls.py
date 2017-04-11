from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.profile_detail, name='profile'),
    url(r'^history', views.history, name='history'),
    url(r'^(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile),
]