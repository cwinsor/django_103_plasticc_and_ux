"""starchaser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from views import welcome, info, signup
from views import ref01_why_game
from views import ref04_variety_of_approaches
from views import ref05_this_web_application
from views import ref06_building_a_model
from views import ref08_plasticc_and_kaggle
from views import ref09_metrics

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^admin/', include(admin.site.urls)),
    path('',  welcome, name='star_chaser_welcome'),
    #url(r'^$', welcome, name='star_chaser_welcome'),
    path('info/', info, name="star_chaser_info"),
    path('player/', include('app_player.urls')),
    #path('login', auth_views.login, name='login'),
    #path('logout', auth_views.logout, name='logout'),
    path('signup', signup, name='signup'),

    path('ref01_why_game', ref01_why_game, name='ref01_why_game'),
    path('ref04_variety_of_approaches', ref04_variety_of_approaches, name='ref04_variety_of_approaches'),
    path('ref05_this_web_application', ref05_this_web_application, name='ref05_this_web_application'),
    path('ref06_building_a_model', ref06_building_a_model, name='ref06_building_a_model'),
    path('ref08_plasticc_and_kaggle', ref08_plasticc_and_kaggle, name='ref08_plasticc_and_kaggle'),
    path('ref09_metrics', ref09_metrics, name='ref09_metrics'),
]
