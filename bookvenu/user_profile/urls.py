from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.profile_detail, name='profile'),
    url(r'^change-password/', views.change_password, name='change-password'),
    url(r'^history/', views.history, name='history'),
]
