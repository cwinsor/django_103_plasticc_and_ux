from django import forms
from django.forms import ModelForm, Form, ValidationError

from app_gameplay.models import PlasticcStar, PlasticcSample, GameplayRound, Bet


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


class BetForm(Form):

    star_id = forms.IntegerField(label='Star IDD', disabled=True)

    bid_1 = forms.IntegerField(
        label='bid_1', initial=56, min_value=0, max_value=100,
        help_text='this is some help text')

    def __init__(self, star_id, df_btrotta, df_kboone):
        super().__init__() 

        self._star_id = star_id
        self._df_btrotta = df_btrotta
        self._df_kboone = df_kboone


    # # reference https://docs.djangoproject.com/en/3.0/ref/forms/validation/#validating-fields-with-clean
    # def clean(self):

    #     cleaned_data = super().clean()

    #     star = cleaned_data.get('star')
    #     user = cleaned_data.get('user')
    #     timestamp = cleaned_data.get('timestamp')

    #     b = []
    #     b.append(cleaned_data.get('bid_1'))
    #     b.append(cleaned_data.get('bid_2'))
    #     b.append(cleaned_data.get('bid_3'))
    #     b.append(cleaned_data.get('bid_4'))
    #     b.append(cleaned_data.get('bid_5'))
    #     b.append(cleaned_data.get('bid_6'))
    #     b.append(cleaned_data.get('bid_7'))
    #     b.append(cleaned_data.get('bid_8'))
    #     b.append(cleaned_data.get('bid_9'))
    #     b.append(cleaned_data.get('bid_10'))
    #     b.append(cleaned_data.get('bid_11'))
    #     b.append(cleaned_data.get('bid_12'))
    #     b.append(cleaned_data.get('bid_13'))
    #     sumb = sum(b)

    #     try:
    #         #game = self.instance.game
    #         if sumb != 100:
    #             raise ValidationError("Bets need to sum to 100")
    #     except IndexError:
    #         raise ValidationError("Index error")
    #     except AttributeError:
    #         raise ValidationError("Attribute error")
    #     return self.cleaned_data
