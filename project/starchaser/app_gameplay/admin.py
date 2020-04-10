from django.contrib import admin

from .models import Profile, PlasticcStar, PlasticcSample, GameplayRound, Bet

admin.site.register(Profile)
admin.site.register(PlasticcStar)
admin.site.register(PlasticcSample)
admin.site.register(GameplayRound)
admin.site.register(Bet)
