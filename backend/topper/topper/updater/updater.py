from abc import abstractmethod
from topper.models import Service, Story


class Updater:

    def __init__(self, service_name):
        self.service = Service.objects.get(name=service_name)

    @abstractmethod
    def update(self):
        pass

    def save(self, story, created):
        if created:
            story.status = Story.NEW
        else:
            story.status = Story.OK

        story.save()





