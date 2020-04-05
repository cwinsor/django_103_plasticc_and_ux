from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, pick_star, place_bet, well_done
from .views import game_info, game_help
from .views import new_plasticc_star, new_plasticc_sample, new_gameplay_round


urlpatterns = [
    path(
        route='',
        view=home),

    path(
        route='home/',
        view=home,
        name="player_home"),

    path(
        route='pick_star/',
        view=pick_star,
        name="player_pick_star"),

    path(
        route='place_bet/<int:id>',
        view=place_bet,
        name="place_bet"),

    path(
        route='well_done/',
        view=well_done,
        name="player_well_done"),

    path(
        route='login/',
        view=LoginView.as_view(template_name='app_player/login_form.html'),
        name='player_login'),

    path(
        route='logout/',
        view=LogoutView.as_view(),
        name='player_logout'),

    path(
        route='game_info/',
        view=game_info,
        name="game_info"),

    path(
        route='game_help/',
        view=game_help,
        name="game_help"),

    path(
        route='add_star/',
        view=new_plasticc_star,
        name="new_plasticc_star"),

    path(
        route='add_sample/',
        view=new_plasticc_sample,
        name="new_plasticc_sample"),

    path(
        route='add_gamplay_round/',
        view=new_gameplay_round,
        name="new_gameplay_round"),

]
