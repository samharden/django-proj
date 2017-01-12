from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views
from crim.view_routes.hills import (hillsborough_dwlsr,
                                    hillsborough_dui,
                                    hillsborough_battery,
                                    hillsborough_petit_theft,
                                    hillsborough_marijuanaposs,
                                    )
from crim.view_routes.pinel import (pinellas_dui,

                                    )


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^fl/hills/hillsborough-dui.html$',
        hillsborough_dui.hillsborough_dui,
        name='hillsborough-dui'),

    url(r'^fl/hills/hillsborough-battery.html$',
        hillsborough_battery.hillsborough_battery,
        name='hillsborough-battery'),

    url(r'^fl/hills/hillsborough-marijuanaposs.html$',
        hillsborough_marijuanaposs.hillsborough_marijuanaposs,
        name='hillsborough-marijuanaposs'),

    url(r'^fl/hills/hillsborough-petit-theft.html$',
        hillsborough_petit_theft.hillsborough_petit_theft,
        name='hillsborough-petit-theft'),

    url(r'^fl/hills/hillsborough-dwlsr.html$',
        hillsborough_dwlsr.hillsborough_dwlsr,
        name='hillsborough-dwlsr'),


    url(r'^fl/pinellas/pinellas-dui.html$',
        pinellas_dui.pinellas_dui,
        name='hillsborough-dui'),

    #url(r'^pinellas.html$', views.pinellas, name='pinellas'),
]
