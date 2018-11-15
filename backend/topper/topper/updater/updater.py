from abc import abstractmethod
from api.models import Service


class Updater:

    def __init__(self, service_name):
        self.service = Service.objects.get(name=service_name)



