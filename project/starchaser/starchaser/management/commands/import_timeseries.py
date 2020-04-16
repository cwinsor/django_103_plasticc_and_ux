from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ValidationError

from app_gameplay.models import PlasticcStar, PlasticcSample

import csv


class Command(BaseCommand):

    help = 'Imports PLAsTiCC timeseries file'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):
        path = options['path'][0]

        self.stdout.write("type=" + str(type(path)))

        fieldnames = 'object_id', 'mjd', 'passband', 'flux', 'flux_err', 'detected'



        with open(path) as csvfile:
            reader = csv.DictReader(f=csvfile, fieldnames=fieldnames)
            count = 0
            for row in reader:
                #self.stdout.write("here0")
                count+=1
                self.stdout.write("{} {}".format(count, row['object_id']))

                # verification and conversion
                # as needed...
                star_id = row['object_id']

                #self.stdout.write(star_id)
                try:
                    star_inst = PlasticcStar.objects.get(pk=star_id)
                    #obj = Class.objects.get(pk=this_object_id)

                    #self.stdout.write("here3" + str(type(star_inst)))

                    #Entry.objects.all()[:10:2]
                    #self.stdout.write("here1{}".format(str(type(x))))

                    # create Model and save
                    plasticcSample = PlasticcSample(
                        star=star_inst,
                        mjd=row['mjd'],
                        passband=row['passband'],
                        flux=row['flux'],
                        flux_err=row['flux_err'],
                        detected=row['detected']
                        )

                    #plasticcSample.full_clean()
                    plasticcSample.save()
                except ValidationError as exc:
                    # if the're a problem anywhere, you wanna know about it
                    self.stdout.write(self.style.NOTICE('there was a problem with line:'))
                    self.stdout.write(str(row))
                    #raise ValidationError("ValidationError...") from exc

                except ValueError as exc:
                    # if the're a problem anywhere, you wanna know about it
                    self.stdout.write(self.style.NOTICE('there was a problem with line:'))
                    self.stdout.write(str(row))
                    #raise ValidationError("ValueError...") from exc


