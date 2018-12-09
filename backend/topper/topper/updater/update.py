from .hacker_news_updater import HackerNewsUpdater
from .reddit_updater import RedditUpdater
from .pocketcasts_updater import PocketCastsUpdater
from .twitter_updater import TwitterUpdater


def update():
    TwitterUpdater().update()
    HackerNewsUpdater().update()
    RedditUpdater().update()
    PocketCastsUpdater().update()


