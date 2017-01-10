from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views
from crim.templates.crim.fl.hills.battery import hillsborough_battery

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hillsborough-dui.html$', views.hillsborough_dui, name='hillsborough-dui'),
    url(r'^fl/hills/hillsborough-battery.html$', views.hillsborough_battery, name='hillsborough-battery'),
    #url(r'^fl/hills/hillsborough-battery.html$', hillsborough_battery, name='hillsborough-battery'),
    url(r'^pinellas.html$', views.pinellas, name='pinellas'),
]
