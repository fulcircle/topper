from django.http import HttpResponse
from topper.updater.reddit_updater import RedditUpdater


# Create your views here.
def update(request):
    result = RedditUpdater().update()
    return HttpResponse("", status=200)

