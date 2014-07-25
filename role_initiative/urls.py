from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin, auth
from django.shortcuts import render

from role_initiative.home import views as home
from role_initiative.login import views as login

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'role_initiative.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', home.home, name='home'),
    url(r'^roll_dice/?$', home.roll_dice, name='roll_dice'),
    url(r'^header/?$', home.header, name='header'),
    url(r'^character/?$', home.character_sheet, name="character_sheet"),

    url(r'^login/?$', login.login, name="login"),
)

