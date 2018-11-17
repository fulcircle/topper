from tastypie import fields
from tastypie.resources import ModelResource
from api.models import Service, Story
import maya


class ServiceResource(ModelResource):
    class Meta:
        queryset = Service.objects.all()
        resource_name = 'service'
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        excludes = ['last_run']


class StoryResource(ModelResource):

    service = fields.ForeignKey(ServiceResource, 'service', full=True)

    class Meta:
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        queryset = Story.objects.all()
        resource_name = 'story'

    def get_object_list(self, request):
        hours_ago_24 = maya.now().subtract(hours=24).datetime()
        return super(StoryResource, self).get_object_list(request).filter(story_date__gte=hours_ago_24)


