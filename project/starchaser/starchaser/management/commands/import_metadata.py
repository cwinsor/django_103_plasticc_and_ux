from django.core.management.base import BaseCommand, CommandError

from app_gameplay.models import PlasticcStar, PlasticcSample

import csv


class Command(BaseCommand):

    help = 'Imports PLAsTiCC metadata file'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):
        path = options['path'][0]

        self.stdout.write("type=" + str(type(path)))

        fieldnames = 'object_id', 'ra', 'decl', 'gal_l', 'gal_b', \
        'ddf', 'hostgal_specz', 'hostgal_photoz', 'hostgal_photoz_err', \
        'distmod', 'mwebv', 'target'

        with open(path) as csvfile:
            reader = csv.DictReader(f=csvfile, fieldnames=fieldnames)
            for row in reader:
                self.stdout.write("{}".format(row['object_id']))

                # verification and conversion
                # as needed...

                # create Model and save
                plasticcStar = PlasticcStar(
                    star_id=row['object_id'],
                    ra=row['ra'],
                    decl=row['decl'],
                    gal_l=row['gal_l'],
                    gal_b=row['gal_b'],
                    ddf=row['ddf'],
                    hostgal_specz=row['hostgal_specz'],
                    hostgal_photoz=row['hostgal_photoz'],
                    hostgal_photoz_err=row['hostgal_photoz_err'],
                    distmod=row['distmod'],
                    MWEBV=row['mwebv'],
                    target=row['target'])
                try:
                    plasticcStar.save()
                except:
                    # if the're a problem anywhere, you wanna know about it
                    self.stdout.write(self.style.NOTICE('there was a problem with line:'))
                    self.stdout.write(str(row))

