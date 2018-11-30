import datetime
import pytz
import praw

from topper.models import Story
from django.conf import settings
from topper.updater.updater import Updater
from django.db import transaction
import urllib.parse


class RedditUpdater(Updater):

    MAX_SUBREDDIT_STORIES = 20

    def __init__(self):
        super().__init__('Reddit')
        self.reddit = praw.Reddit(client_id=settings.REDDIT['client_id'],
                                  client_secret=settings.REDDIT['client_secret'],
                                  password=settings.REDDIT['password'],
                                  user_agent='topper by /u/evilturnip',
                                  username=settings.REDDIT['username'])

    @transaction.atomic
    def update(self):
        for subreddit in self.reddit.user.subreddits():
            stories = 0
            for data in subreddit.top('day'):
                if stories > self.MAX_SUBREDDIT_STORIES:
                    break

                stories += 1
                story, created = Story.objects.get_or_create(service=self.service,
                                                                      code=data.id,
                                                                      category=subreddit)

                story.title = data.title

                story.story_date = datetime.datetime.utcfromtimestamp(data.created_utc).replace(tzinfo=pytz.UTC)

                story.score = data.score

                story.url = data.url
                story.comments_url = urllib.parse.urljoin(self.service.url,  data.permalink)

                story.comments = data.num_comments

                self.save(story, created)
