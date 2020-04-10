import numpy as np
import pandas as pd

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from app_gameplay.models import GameplayRound, PlasticcStar
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

    num_stars = 10
    num_starclasses = 13

    the_data = PlasticcStar.objects.random_set(num_stars)

    the_table = pd.DataFrame(
        columns=['starId']
        data=the_data
    )

      evals_btrotta = pd.DataFrame(
        data=np.random.randint(0, 100, size=(13, 2)),
        columns=['star00','star01']
        ).T



    stars_available = PlasticcStar.objects.random_set()
    stars_available_list = list(stars_available)[:num_stars]

    # example
    # df = pd.DataFrame(np.random.randint(0,100,size=(15, 4)), columns=list('ABCD'))
    evals_btrotta = pd.DataFrame(
        data=np.random.randint(0, 100, size=(13, 2)),
        columns=['star00','star01']
        ).T
    evals_btrotta = evals_btrotta.T
    evals_btrotta_html = evals_btrotta.to_html()
    evals_btrotta_list = evals_btrotta.to_numpy().tolist()

    evals_kboone = [[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
                    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]]
    return render(request, "app_player/pick_star.html",
                  {'stars_available': stars_available_list,
                   'evals_btrotta_html': evals_btrotta_html,
                   'evals_btrotta_list': evals_btrotta_list,
                   'evals_kboone': evals_kboone}
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
