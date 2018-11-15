from django.http import HttpResponse

from topper.updater.hacker_news_updater import HackerNewsUpdater
# Create your views here.
def update(request):
    result = HackerNewsUpdater().update()
    return HttpResponse("", status=200)

