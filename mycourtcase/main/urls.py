from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^$', auth_views.login, name='homepage'),
    url(r'^search.html', views.search_page, name='search'),
]



# urlpatterns = [
#     url(r'^$', views.home_page, name='homepage'),
#
# ]
