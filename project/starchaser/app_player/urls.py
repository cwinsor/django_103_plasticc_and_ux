from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, pick_star, new_bet, well_done
from .views import game_info, game_help
from .views import new_plasticc_star, new_plasticc_sample, new_gameplay_round


urlpatterns = [
    path(
        '',
        home),

    path(
        'home/',
        home,
        name="player_home"),

    path(
        'pick_star/',
        pick_star,
        name="player_pick_star"),

    path(
        'place_bet/',
        new_bet,
        name="new_bet"),

    path(
        'well_done/',
        well_done,
        name="player_well_done"),

    path(
        'login/',
        LoginView.as_view(template_name='app_player/login_form.html'),
        name='player_login'),

    path(
        'logout/',
        LogoutView.as_view(),
        name='player_logout'),

    path(
        'game_info/',
        game_info,
        name="game_info"),

    path(
        'game_help/',
        game_help,
        name="game_help"),

    path(
        'add_star/',
        new_plasticc_star,
        name="new_plasticc_star"),

    path(
        'add_sample/',
        new_plasticc_sample,
        name="new_plasticc_sample"),

    path(
        'add_gamplay_round/',
        new_gameplay_round,
        name="new_gameplay_round"),

]
