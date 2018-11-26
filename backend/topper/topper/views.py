from django.http import HttpResponse
from topper.updater.pocketcasts_updater import PocketCastsUpdater
from topper.updater.reddit_updater import RedditUpdater
from topper.updater.hacker_news_updater import HackerNewsUpdater


# Create your views here.
def update(request):
    PocketCastsUpdater().update()
    RedditUpdater().update()
    HackerNewsUpdater().update()

    return HttpResponse("", status=200)

