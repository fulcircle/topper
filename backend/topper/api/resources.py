# api/resources.py
from tastypie.resources import ModelResource
from api.models import Service


class ServiceResource(ModelResource):
    class Meta:
        queryset = Service.objects.all()
        resource_name = 'service'
