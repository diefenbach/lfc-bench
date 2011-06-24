# django imports
from django.core.management.base import BaseCommand

# lfc imports
from django.contrib.auth.models import User


class Command(BaseCommand):
    args = ""
    help = """"""

    def handle(self, *args, **options):
        for i in range(1, 100):
            User.objects.create(username="username-%s" % i)