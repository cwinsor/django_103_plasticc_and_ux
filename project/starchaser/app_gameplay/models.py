import numpy as np

from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

fmt = '{}'
# fmt_f = '{:5.2f}'
fmt_f = '{:.2f}'
fmt_starid = '{:8}'
fmt_betid = '{:8}'
fmt_is = '{:1}'
fmt_i3 = '{:3}'


# a subclass of QuerySet representing a subset of PlasticcStar
class PlasticcStarQuerySet(models.QuerySet):

    def random_set(self):

        #qs = self.filter(target__exact=92)
        # order_by("?").first()
        #star42 = self.filter(target__exact=42).order_by("?").first()
        #star4 = qs.order_by("?").first()

        star00 = self.filter(target__exact=90).order_by("?").first().star_id
        star01 = self.filter(target__exact=42).order_by("?").first().star_id
        star02 = self.filter(target__exact=65).order_by("?").first().star_id
        star03 = self.filter(target__exact=16).order_by("?").first().star_id
        star04 = self.filter(target__exact=15).order_by("?").first().star_id
        star05 = self.filter(target__exact=62).order_by("?").first().star_id
        star06 = self.filter(target__exact=88).order_by("?").first().star_id
        star07 = self.filter(target__exact=92).order_by("?").first().star_id
        star08 = self.filter(target__exact=67).order_by("?").first().star_id
        star09 = self.filter(target__exact=52).order_by("?").first().star_id
        star10 = self.filter(target__exact=95).order_by("?").first().star_id
        star11 = self.filter(target__exact=6).order_by("?").first().star_id
        star12 = self.filter(target__exact=64).order_by("?").first().star_id
        star13 = self.filter(target__exact=53).order_by("?").first().star_id

        #90   (2313, 12)
        #42   (1193, 12)
        #65   (981, 12)
        #16   (924, 12)
        #15   (495, 12)
        #62   (484, 12)
        #88   (370, 12)
        #92   (239, 12)
        #67   (208, 12)
        #52   (183, 12)
        #95   (175, 12)
        #6    (151, 12)
        #64   (102, 12)
        #53   (30, 12)

        return np.array([
            star00,
            star01,
            star02,
            star03,
            star04,
            star05,
            star06,
            star07,
            star08,
            star09,
            star10,
            star11,
            star12,
            star13,
       ])
        # return self.all()


class PlasticcStar(models.Model):

    # override "objects" property replacing it with custom QuerySet
    objects = PlasticcStarQuerySet.as_manager()

    star_id = models.IntegerField(primary_key=True)
    ra = models.FloatField()
    decl = models.FloatField()
    gal_l = models.FloatField()
    gal_b = models.FloatField()
    ddf = models.BooleanField()
    hostgal_specz = models.FloatField()
    hostgal_photoz = models.FloatField()
    hostgal_photoz_err = models.FloatField()
    distmod = models.FloatField()
    MWEBV = models.FloatField()
    target = models.SmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        msg = ' star_id ' + fmt_starid
        msg += ' ra ' + fmt_f
        msg += ' decl ' + fmt_f
        msg += ' gal_l ' + fmt_f
        msg += ' gal_b ' + fmt_f
        msg += ' ddf ' + fmt_f
        msg += ' hgal_s ' + fmt_f
        msg += ' hgal_p ' + fmt_f
        msg += ' p_err ' + fmt_f
        msg += ' dist ' + fmt_f
        msg += ' mw_ebv ' + fmt_f
        msg += ' class ' + fmt_is

        return msg.format(
            self.star_id,
            self.ra,
            self.decl,
            self.gal_l,
            self.gal_b,
            self.ddf,
            self.hostgal_specz,
            self.hostgal_photoz,
            self.hostgal_photoz_err,
            self.distmod,
            self.MWEBV,
            self.target)


class PlasticcSample(models.Model):
    star = models.ForeignKey(
        PlasticcStar,
        on_delete=models.CASCADE)
    mjd = models.FloatField(default=0)
    passband = models.SmallIntegerField()
    flux = models.FloatField()
    flux_err = models.FloatField()
    detected = models.BooleanField()

    import_order = ["id", "star", "mjd", "passband", "flux",
                    "flux_err", "detected"]
    export_order = ["id", "star", "mjd", "passband", "flux",
                    "flux_err", "detected"]

    def __str__(self):
        msg = '{}'
        msg += ' star_id ' + fmt_starid
        msg += ' mjd ' + fmt
        msg += ' passband ' + fmt_is
        msg += ' flux ' + fmt_f
        msg += ' f_err ' + fmt_f
        msg += ' detected ' + fmt

        return msg.format(
            self.id,
            self.star.star_id,
            self.mjd,
            self.passband,
            self.flux,
            self.flux_err,
            self.detected)


# a subclass of QuerySet representing all GameplayRounds
# with method (for example) that returns all games for user
class GameplayRoundQuerySet(models.QuerySet):

    def rounds_this_player(self, user):
        return self.filter(
            Q(player=user)
        )


class Bet(models.Model):

    star = models.ForeignKey(
        PlasticcStar,
        related_name="the_star",
        on_delete=models.CASCADE)

    user = models.ForeignKey(
        User,
        related_name="the_user",
        on_delete=models.CASCADE)

    timestamp = models.DateTimeField(
        auto_now_add=True)

    bid_a = models.SmallIntegerField(
        null=False, default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)])
    bid_b = models.SmallIntegerField(
        null=False, default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)])
    bid_c = models.SmallIntegerField(
        null=False, default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)])
    bid_d = models.SmallIntegerField(
        null=False, default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)])
    bid_e = models.SmallIntegerField(
        null=False, default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)])
    bid_f = models.SmallIntegerField(
        null=False, default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)])
    bid_g = models.SmallIntegerField(
        null=False, default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)])
    bid_h = models.SmallIntegerField(
        null=False, default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)])
    bid_i = models.SmallIntegerField(
        null=False, default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)])
    bid_j = models.SmallIntegerField(
        null=False, default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)])
    bid_k = models.SmallIntegerField(
        null=False, default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)])
    bid_l = models.SmallIntegerField(
        null=False, default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)])
    bid_m = models.SmallIntegerField(
        null=False, default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)])

    def __str__(self):

        msg = ''
        msg += '{}'
        msg += ' user: {}'
        msg += ' star: {} ='
        msg += ' {}'
        msg += ' {}'
        msg += ' {}'
        msg += ' {}'
        msg += ' {}'
        msg += ' {}'
        msg += ' {}'
        msg += ' {}'
        msg += ' {}'
        msg += ' {}'
        msg += ' {}'
        msg += ' {}'
        msg += ' {}'

        temp = msg.format(
            self.id,
            self.user.username,
            self.star.star_id,
            self.bid_a,
            self.bid_b,
            self.bid_c,
            self.bid_d,
            self.bid_e,
            self.bid_f,
            self.bid_g,
            self.bid_h,
            self.bid_i,
            self.bid_j,
            self.bid_k,
            self.bid_l,
            self.bid_m)

        return temp


class GameplayRound(models.Model):

    # override "objects" property replacing it with custom QuerySet
    objects = GameplayRoundQuerySet.as_manager()

    name = models.CharField(max_length=10)

    player = models.ForeignKey(
        User,
        related_name="player",
        on_delete=models.CASCADE)

    bet = models.ForeignKey(
        Bet,
        related_name="bet",
        on_delete=models.CASCADE)

    def __str__(self):
        msg = '{}'
        msg += ' "{:10}"'
        msg += ' bet ' + fmt_betid

        return msg.format(
            self.id,
            self.name,
            self.bet.id)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_score = models.IntegerField(default=0)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
