from django.conf.urls import url
from .filters import JobFilter
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^register$', views.register),
    url(r'^register-page$', views.register_page),
    url(r'^login-page$', views.login_page)
]