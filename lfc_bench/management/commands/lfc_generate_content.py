# django imports
from django.core.management.base import BaseCommand

# lfc imports
from lfc.models import Page


class Command(BaseCommand):
    args = ""
    help = """"""

    def handle(self, *args, **options):
        for i in range(1, 11):
            parent = Page.objects.create(title="Page %s" % i, slug="page-%s" % i)

            for i in range(1, 30):
                Page.objects.create(title="Page %s" % i, slug="page-%s" % i, parent=parent)

