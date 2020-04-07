import logging

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


class BetForm(ModelForm):

    class Meta:
        model = Bet
        #exclude = ()
        fields = [
            'star',
            'user',
            # 'timestamp',
            'bid_a',
            'bid_b',
            'bid_c',
            'bid_d',
            'bid_e',
            'bid_f',
            'bid_g',
            'bid_h',
            'bid_i',
            'bid_j',
            'bid_k',
            'bid_l',
            'bid_m'] 

    def clean_foo(self):
        raise forms.ValidationError("i tried foo and do not like it")


    #user = forms.CharField      (required=False, label='user', disabled=True)
    #star_id = forms.IntegerField(required=False, label='object_id', disabled=True)

    #bid_a1 = forms.IntegerField(required=False, label='bid_a1', min_value=0, max_value=100)
    #bid_b1 = forms.IntegerField(required=False, label='bid_b1', min_value=0, max_value=100)
    #bid_c1 = forms.IntegerField(required=False, label='bid_c1', min_value=0, max_value=100)

    bid_a2 = forms.IntegerField(required=False, label='bid_a2', min_value=0, max_value=100, disabled=True)
    bid_b2 = forms.IntegerField(required=False, label='bid_b2', min_value=0, max_value=100, disabled=True)
    bid_c2 = forms.IntegerField(required=False, label='bid_c2', min_value=0, max_value=100, disabled=True)
    bid_d2 = forms.IntegerField(required=False, label='bid_d2', min_value=0, max_value=100, disabled=True)
    bid_e2 = forms.IntegerField(required=False, label='bid_e2', min_value=0, max_value=100, disabled=True)
    bid_f2 = forms.IntegerField(required=False, label='bid_f2', min_value=0, max_value=100, disabled=True)
    bid_g2 = forms.IntegerField(required=False, label='bid_g2', min_value=0, max_value=100, disabled=True)
    bid_h2 = forms.IntegerField(required=False, label='bid_h2', min_value=0, max_value=100, disabled=True)
    bid_i2 = forms.IntegerField(required=False, label='bid_i2', min_value=0, max_value=100, disabled=True)
    bid_j2 = forms.IntegerField(required=False, label='bid_j2', min_value=0, max_value=100, disabled=True)
    bid_k2 = forms.IntegerField(required=False, label='bid_k2', min_value=0, max_value=100, disabled=True)
    bid_l2 = forms.IntegerField(required=False, label='bid_l2', min_value=0, max_value=100, disabled=True)
    bid_m2 = forms.IntegerField(required=False, label='bid_m2', min_value=0, max_value=100, disabled=True)

    bid_a3 = forms.IntegerField(required=False, label='bid_a3', min_value=0, max_value=100, disabled=True)
    bid_b3 = forms.IntegerField(required=False, label='bid_b3', min_value=0, max_value=100, disabled=True)
    bid_c3 = forms.IntegerField(required=False, label='bid_c3', min_value=0, max_value=100, disabled=True)
    bid_d3 = forms.IntegerField(required=False, label='bid_d3', min_value=0, max_value=100, disabled=True)
    bid_e3 = forms.IntegerField(required=False, label='bid_e3', min_value=0, max_value=100, disabled=True)
    bid_f3 = forms.IntegerField(required=False, label='bid_f3', min_value=0, max_value=100, disabled=True)
    bid_g3 = forms.IntegerField(required=False, label='bid_g3', min_value=0, max_value=100, disabled=True)
    bid_h3 = forms.IntegerField(required=False, label='bid_h3', min_value=0, max_value=100, disabled=True)
    bid_i3 = forms.IntegerField(required=False, label='bid_i3', min_value=0, max_value=100, disabled=True)
    bid_j3 = forms.IntegerField(required=False, label='bid_j3', min_value=0, max_value=100, disabled=True)
    bid_k3 = forms.IntegerField(required=False, label='bid_k3', min_value=0, max_value=100, disabled=True)
    bid_l3 = forms.IntegerField(required=False, label='bid_l3', min_value=0, max_value=100, disabled=True)
    bid_m3 = forms.IntegerField(required=False, label='bid_m3', min_value=0, max_value=100, disabled=True)

    sum_1 = forms.IntegerField(required=False, label='sum_1', min_value=0, max_value=100, disabled=True)
    #sum_2 = forms.IntegerField(required=False, label='sum_2', min_value=0, max_value=100, disabled=True)
    #sum_3 = forms.IntegerField(required=False, label='sum_3', min_value=0, max_value=100, disabled=True)
    # zona temporary...
    #sum1=1
    #sum2=2
    #sum3=3

    # reference https://docs.djangoproject.com/en/3.0/ref/forms/validation/#validating-fields-with-clean
    def clean(self):

        cleaned_data = super().clean()

        the_sum = cleaned_data.get('sum_1')

        try:
            #if sumb != 100:
            if the_sum != 100:
                raise ValidationError('Bets need to sum to 100', code='sum_bets_ne_100')
        except IndexError:
            raise ValidationError("Index error")
        except AttributeError:
            raise ValidationError("Attribute error")
        return self.cleaned_data
