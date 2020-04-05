import numpy as np
import pandas as pd
import logging

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from app_gameplay.models import GameplayRound, PlasticcStar
from app_gameplay.present_pick_star import PresentPickStar
from .forms import PlasticcStarForm, PlasticcSampleForm, GameplayRoundForm, BetForm


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
    qs_star = PlasticcStar.objects.random_set(chooser_list_size)

    return render(
            request=request,
            template_name="app_player/pick_staaar.html",
            context={
                'qs_star': qs_star
                }
    )

    ############# the rest is not currently used
    columns = [
        'star_id', 'ra', 'decl', 'hostgal_specz', 'target']
    qs_star = PlasticcStar.objects.random_set(chooser_list_size)
    qs_star_values_allfields = qs_star.values(*columns)

    df_btrotta = pd.DataFrame(
        data=np.random.randint(0, 100, size=(chooser_list_size, 14)),
        columns=['a', 'b', 'c', 'd', 'e', 'f',
                 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
        #columns=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    )
    df_btrotta.loc[[0], ['a']] = 100
    df_btrotta.loc[[1], ['a']] = 101

    df_kboone = pd.DataFrame(
        data=np.random.randint(0, 100, size=(chooser_list_size, 14)),
        columns=['a', 'b', 'c', 'd', 'e', 'f',
                 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
        # columns=['0','1','2','3','4','5','6','7','8','9','10','11','12','13']
        #columns=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    )
    df_kboone.loc[[0], ['a']] = 100
    df_kboone.loc[[1], ['a']] = 101

    present_pick_star = PresentPickStar(qs_star, df_btrotta, df_kboone)

    return render(
        request,
        "app_player/pick_star.html",
        {
            'present_pick_star': present_pick_star
        }
    )


@login_required
def new_bet(request, id):
    
    #logger = logging.getLogger(__name__)
    #logger.debug("\n---here8")
    #logger.debug("\n" + str(request))

    star = get_object_or_404(PlasticcStar, pk=id)

    ###### POST #####
    if request.method == "POST":

        form = BetForm(data=request.POST)
        bet_form_set_disabled_fields(form, request, star)
        bet_form_set_reduction_fields(form, request)

        if form.is_valid():
            #form.save()  # save to db.. to be implemented becuase this is not based on model...
            return redirect('player_well_done')


    ###### GET #####
    else:

        # ======== get non-user-provided bid data (DataFrames)
        df_btrotta = pd.DataFrame(
            data=np.random.randint(0, 100, size=(1, 14)),
            columns=['a', 'b', 'c', 'd', 'e', 'f',
                    'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
        )
        df_kboone = pd.DataFrame(
            data=np.random.randint(0, 100, size=(1, 14)),
            columns=['a', 'b', 'c', 'd', 'e', 'f',
                    'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
        )

        form = BetForm()
        bet_form_set_enabled_fields(form)
        bet_form_set_disabled_fields(form, request, star)
        bet_form_set_reduction_fields(form, request)

    context = {}
    context['form'] = form
    context['star_id'] = star.star_id

    return render(
        request=request,
        template_name="app_player/bet_form.html",
        context=context)


# on the bet form, set the fields that are enabled
# this only needs to happen on GET as a POST provides this data in request.POST
def bet_form_set_enabled_fields(form):

    form.fields['bid_a1'].initial = 0
    form.fields['bid_b1'].initial = 0
    form.fields['bid_c1'].initial = 0


# on the bet form, set the fields that are disabled
# this needs to happen on both GET and POST as POST does not provides this data in request.POST
def bet_form_set_disabled_fields(form, request, star):

    form.fields['user'].initial = request.user
    form.fields['star_id'].initial = star.star_id

    form.fields['bid_a2'].initial = 4 #btrotta
    form.fields['bid_b2'].initial = 5
    form.fields['bid_c2'].initial = 6

    form.fields['bid_a3'].initial = 7 #kboone
    form.fields['bid_b3'].initial = 8
    form.fields['bid_c3'].initial = 9


def bet_form_set_reduction_fields(form, request):
    if request.method == "POST":
        sum = int(request.POST.get("bid_a1")) + \
            int(request.POST.get("bid_b1")) + \
            int(request.POST.get("bid_c1"))
        form.fields['sum_1'].initial = sum
    else:
        form.fields['sum_1'].initial = 0



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
