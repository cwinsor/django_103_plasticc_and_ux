from django.forms import ModelForm

from app_gameplay.models import PlasticcStar, PlasticcSample, GameplayRound


class PlasticcStarForm(ModelForm):
    class Meta:
        model = PlasticcStar
        exclude = ()
        # exclude = ('from_user', 'timestamp')


class PlasticcSampleForm(ModelForm):
    class Meta:
        model = PlasticcSample
        exclude = ()


class GameplayRoundForm(ModelForm):
    class Meta:
        model = GameplayRound
        exclude = ()
