from django.contrib import admin

from .models import PlasticcStar, PlasticcSample, GameplayRound, Profile
admin.site.register(PlasticcStar)
admin.site.register(PlasticcSample)
admin.site.register(GameplayRound)
admin.site.register(Profile)