from django.http import HttpResponse
from topper.updater.update import update as update_sources


# Create your views here.
def update(request):
    update_sources()
    return HttpResponse("", status=200)

