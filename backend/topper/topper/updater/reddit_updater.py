import datetime
import pytz
import praw
from topper.keys import REDDIT
from api.models import SubredditStory
from topper.updater.updater import Updater


class RedditUpdater(Updater):

    MAX_SUBREDDIT_STORIES = 20

    def __init__(self):
        super().__init__('Reddit')
        self.reddit = praw.Reddit(client_id=REDDIT['client_id'],
                                  client_secret=REDDIT['client_secret'],
                                  password=REDDIT['password'],
                                  user_agent='topper by /u/evilturnip',
                                  username=REDDIT['username'])

    def update(self):
        for subreddit in self.reddit.user.subreddits():
            stories = 0
            for data in subreddit.top('day'):
                if stories > self.MAX_SUBREDDIT_STORIES:
                    break

                stories += 1
                story, created = SubredditStory.objects.get_or_create(service=self.service,
                                                                      code=data.id,
                                                                      subreddit=subreddit)

                story.title = data.title

                story.story_date = datetime.datetime.utcfromtimestamp(data.created_utc).replace(tzinfo=pytz.UTC)

                story.score = data.score

                story.url = data.url

                story.comments = data.num_comments

                self.save(story, created)
