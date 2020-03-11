from django.contrib.auth.models import User
from django.shortcuts import render

from app_gameplay.models import GameplayRound

def home(request):

# working on extending the user model to add "total_score" and 
# get that to the home view

# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone




#     top_10_players = GameplayRound.objects.order_by('-total_score')[:10]
# ordered_authors = Author.objects.order_by('-score', 'last_name')[:30]


    rounds_this_player = GameplayRound.objects.filter(
        player=request.user)
    rounds_this_player_list = list(rounds_this_player)

    leader_board = User.objects.all()
    leader_board_list = list(leader_board)

    return render(request, "app_player/home.html",
                  {'rounds': rounds_this_player_list,
                   'leader_board': leader_board_list}

                  )
