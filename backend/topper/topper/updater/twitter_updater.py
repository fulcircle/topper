from django.db import transaction
from django.conf import settings
from topper.updater.updater import Updater
import twitter


class TwitterUpdater(Updater):

    MAX_STORIES = 15

    def __init__(self):
        super().__init__('Twitter')
        self.api = twitter.Api(consumer_key=settings.TWITTER['consumer_key'],
                               consumer_secret=settings.TWITTER['consumer_secret'],
                               access_token_key=settings.TWITTER['access_token_key'],
                               access_token_secret=settings.TWITTER['access_token_secret'])

    @transaction.atomic
    def update(self):
        pass





