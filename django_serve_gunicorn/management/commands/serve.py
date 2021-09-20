from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Run a gunicorn server"

    def add_arguments(self, parser):
        pass
        # parser.add_argument("...", nargs="+", type=int)

    def handle(self, *args, **options):
        print("Hello world")
