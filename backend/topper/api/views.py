from django.http import HttpResponse
from topper.updater.pocketcasts_updater import PocketCastsUpdater


# Create your views here.
def update(request):
    result = PocketCastsUpdater().update()
    return HttpResponse("", status=200)

