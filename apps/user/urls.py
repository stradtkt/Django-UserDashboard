from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^register$', views.register),
    url(r'^register-page$', views.register_page),
    url(r'^login-page$', views.login_page),
    url(r'^dashboard$', views.dashboard),
    url(r'^dashboard/profile/(?P<id>\d+)$', views.profile),
    url(r'^dashboard/profile/(?P<id>\d+)/process_message$', views.process_message),
    url(r'^dashboard/delete-user/(?P<id>\d+)$', views.delete_user),
]