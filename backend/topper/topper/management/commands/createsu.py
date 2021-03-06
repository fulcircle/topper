from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(settings.SUPERUSER['name'], settings.SUPERUSER['email'], settings.SUPERUSER['password'])
