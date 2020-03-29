import numpy as np
import pandas as pd
import logging

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from app_gameplay.models import GameplayRound, PlasticcStar
from app_gameplay.present_pick_star import PresentPickStar
from .forms import PlasticcStarForm, PlasticcSampleForm, GameplayRoundForm


@login_required
def home(request):

    rounds_this_player = GameplayRound.objects.rounds_this_player(request.user)

    leader_board = User.objects.all()
    leader_board_list = list(leader_board)

    return render(request, "app_player/home.html",
                  {'rounds': rounds_this_player,
                   'leader_board': leader_board_list}
                  )


@login_required
def pick_star(request):

    chooser_list_size = 2
    columns = [
        'star_id', 'ra', 'decl', 'hostgal_specz', 'target']
    qs_star = PlasticcStar.objects.random_set(chooser_list_size)
    qs_star_values_allfields = qs_star.values(*columns)

    df_btrotta = pd.DataFrame(
        data=np.random.randint(0, 100, size=(chooser_list_size, 14)),
        columns=['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        #columns=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        )
    df_btrotta.loc[[0], ['a']] = 100
    df_btrotta.loc[[1], ['a']] = 101

    df_kboone = pd.DataFrame(
        data=np.random.randint(0, 100, size=(chooser_list_size, 14)),
        columns=['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        #columns=['0','1','2','3','4','5','6','7','8','9','10','11','12','13']
        #columns=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        )
    df_kboone.loc[[0], ['a']] = 100
    df_kboone.loc[[1], ['a']] = 101

    present_pick_star = PresentPickStar(qs_star, df_btrotta, df_kboone)
    #logger = logging.getLogger(__name__)
    #logger.debug("\n---here7\n" + str(present_pick_star.star_hdr()))
    #logger.debug("\n---here8\n" + str(len(present_pick_star.star_hdr())))

    return render(
        request,
        "app_player/pick_star.html",
        {
            'present_pick_star': present_pick_star
            }
        )


@login_required
def place_bets(request):
    return render(request, "app_player/place_bets.html")


@login_required
def well_done(request):
    return render(request, "app_player/well_done.html")


@login_required
def game_info(request):
    return render(request, "app_player/game_info.html")


@login_required
def game_help(request):
    return render(request, "app_player/game_help.html")


@login_required
def new_plasticc_star(request):
    if request.method == "POST":
        form = PlasticcStarForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_home')
        pass
    else:
        form = PlasticcStarForm()
    return render(request, "app_player/new_plasticc_star_form.html", {'form': form})


@login_required
def new_plasticc_sample(request):
    if request.method == "POST":
        form = PlasticcSampleForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_home')
        pass
    else:
        form = PlasticcSampleForm()
    return render(request, "app_player/new_plasticc_sample_form.html", {'form': form})


@login_required
def new_gameplay_round(request):
    if request.method == "POST":
        form = GameplayRoundForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_home')
        pass
    else:
        form = GameplayRoundForm()
    return render(request, "app_player/new_gameplay_round_form.html", {'form': form})
