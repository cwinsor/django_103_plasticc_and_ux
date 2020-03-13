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
fmt_is = '{:1}'
fmt_i3 = '{:3}'


class PlasticcStar(models.Model):
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
    mjd = models.DateTimeField()
    passband = models.SmallIntegerField()
    flux = models.FloatField()
    flux_err = models.FloatField()
    detected = models.BooleanField()

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


class GameplayRound(models.Model):
    player = models.ForeignKey(
        User,
        related_name="player",
        on_delete=models.CASCADE)
    star = models.ForeignKey(
        PlasticcStar,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    bid_1 = models.SmallIntegerField(null=False, default=0, validators=[
                                     MinValueValidator(0), MaxValueValidator(100)])
    bid_2 = models.SmallIntegerField(null=False, default=0, validators=[
                                     MinValueValidator(0), MaxValueValidator(100)])
    bid_3 = models.SmallIntegerField(null=False, default=0, validators=[
                                     MinValueValidator(0), MaxValueValidator(100)])
    bid_4 = models.SmallIntegerField(null=False, default=0, validators=[
                                     MinValueValidator(0), MaxValueValidator(100)])
    bid_5 = models.SmallIntegerField(null=False, default=0, validators=[
                                     MinValueValidator(0), MaxValueValidator(100)])
    bid_6 = models.SmallIntegerField(null=False, default=0, validators=[
                                     MinValueValidator(0), MaxValueValidator(100)])
    bid_7 = models.SmallIntegerField(null=False, default=0, validators=[
                                     MinValueValidator(0), MaxValueValidator(100)])
    bid_8 = models.SmallIntegerField(null=False, default=0, validators=[
                                     MinValueValidator(0), MaxValueValidator(100)])
    bid_9 = models.SmallIntegerField(null=False, default=0, validators=[
                                     MinValueValidator(0), MaxValueValidator(100)])
    bid_10 = models.SmallIntegerField(null=False, default=0, validators=[
                                      MinValueValidator(0), MaxValueValidator(100)])
    bid_11 = models.SmallIntegerField(null=False, default=0, validators=[
                                      MinValueValidator(0), MaxValueValidator(100)])
    bid_12 = models.SmallIntegerField(null=False, default=0, validators=[
                                      MinValueValidator(0), MaxValueValidator(100)])
    bid_13 = models.SmallIntegerField(null=False, default=0, validators=[
                                      MinValueValidator(0), MaxValueValidator(100)])

    # override "objects" property replacing it with custom QuerySet
    objects = GameplayRoundQuerySet.as_manager()

    def __str__(self):
        msg = '{}'
        msg += ' "{:10}"'
        msg += ' star_id ' + fmt_starid
        msg += ' bets:' + fmt_i3
        msg += ' ' + fmt_i3
        msg += ' ' + fmt_i3
        msg += ' ' + fmt_i3
        msg += ' ' + fmt_i3
        msg += ' ' + fmt_i3
        msg += ' ' + fmt_i3
        msg += ' ' + fmt_i3
        msg += ' ' + fmt_i3
        msg += ' ' + fmt_i3
        msg += ' ' + fmt_i3
        msg += ' ' + fmt_i3
        msg += ' ' + fmt_i3

        return msg.format(
            self.id,
            self.name,
            self.star.star_id,
            self.bid_1,
            self.bid_2,
            self.bid_3,
            self.bid_4,
            self.bid_5,
            self.bid_6,
            self.bid_7,
            self.bid_8,
            self.bid_9,
            self.bid_10,
            self.bid_11,
            self.bid_12,
            self.bid_13)


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
