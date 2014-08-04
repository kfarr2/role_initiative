from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin, auth
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from role_initiative.home import views as home
from role_initiative.featured_games import views as featured_games
from role_initiative.users import views as users

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'role_initiative.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', home.home, name='home'),
    url(r'^logout/?$', 'django.contrib.auth.views.logout', {"next_page": reverse_lazy("home")}, name="logout"),

    url(r'^roll_dice/?$', home.roll_dice, name='roll_dice'),
    url(r'^header/?$', home.header, name='header'),
    url(r'^character/?$', home.character_sheet, name="character_sheet"),

    url(r'^login/?$', users.login, name="users-login"),
    url(r'^login/new/?$', users.create, name="users-create"),

    url(r'^featured_games/?$', featured_games.game_view, name="featured_games-list"),
    url(r'^featured_games/create/?$', featured_games.create, name='featured_games-create'),
)

