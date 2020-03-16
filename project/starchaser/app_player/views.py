from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from app_gameplay.models import GameplayRound
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
    return render(request, "app_player/pick_star.html")


@login_required
def place_bets(request):
    return render(request, "app_player/place_bets.html")


@login_required
def well_done(request):
    return render(request, "app_player/well_done.html")


@login_required
def new_plasticc_star(request):
    form = PlasticcStarForm()
    return render(request, "app_player/new_plasticc_star.html", {'form': form})


@login_required
def new_plasticc_sample(request):
    form = PlasticcSampleForm()
    return render(request, "app_player/new_plasticc_sample.html", {'form': form})


@login_required
def new_gameplay_round(request):
    form = GameplayRoundForm()
    return render(request, "app_player/new_gameplay_round.html", {'form': form})

