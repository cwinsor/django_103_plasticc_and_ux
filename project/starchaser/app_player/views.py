from django.contrib.auth.models import User
from django.shortcuts import render, redirect
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
    if request.method == "POST":
        form = PlasticcStarForm(data = request.POST)
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
        form = PlasticcSampleForm(data = request.POST)
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
        form = GameplayRoundForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_home')
        pass
    else:
        form = GameplayRoundForm()
    return render(request, "app_player/new_gameplay_round_form.html", {'form': form})

