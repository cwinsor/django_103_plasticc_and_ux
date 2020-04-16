from django.core.management.base import BaseCommand, CommandError

from app_gameplay.models import PlasticcStar, PlasticcSample

import csv


class Command(BaseCommand):

    help = 'Does whatever'

    def add_arguments(self, parser):
        parser.add_argument('argument123', nargs='+', type=str)

    def handle(self, *args, **options):
        argument = options['argument123'][0]

        self.stdout.write(self.style.SUCCESS('SUCCESS - hello from Whatever ' + str(argument)))
        self.stdout.write(self.style.ERROR(  'ERROR   - hello from Whatever ' + str(argument)))
        self.stdout.write(self.style.NOTICE( 'NOTICE  - hello from Whatever ' + str(argument)))
        self.stdout.write('hello from Whatever ' + str(argument))