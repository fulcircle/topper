from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from topper.settings import SUPERUSER


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(SUPERUSER['name'], SUPERUSER['email'], SUPERUSER['password'])
