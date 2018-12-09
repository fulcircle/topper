from .hacker_news_updater import HackerNewsUpdater
from .reddit_updater import RedditUpdater
from .pocketcasts_updater import PocketCastsUpdater
from .twitter_updater import TwitterUpdater
from topper.exception_handler import ExceptionHandler


def update():
    updaters = [TwitterUpdater, HackerNewsUpdater, RedditUpdater, PocketCastsUpdater]
    for updater in updaters:
        try:
            updater().update()
        except Exception as e:
            ExceptionHandler().handle_exception(e)
            continue


