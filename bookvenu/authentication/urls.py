from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^register/', views.register_page, name='register'),
    url(r'^profile/change-password/', views.change_password, name='change-password'),
]

