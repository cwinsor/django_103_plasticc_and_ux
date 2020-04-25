
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="cwinsor").exists():
            User.objects.create_superuser("cwinsor", "cwinsor@gmail.com", "abc123")
        if not User.objects.filter(username="cwinsor2").exists():
            User.objects.create_superuser("cwinsor2", "cwinsor@gmail.com", "abc123")
