from tastypie import fields
from tastypie.resources import ModelResource
from api.models import Service, Story, Podcast
import maya


class ServiceResource(ModelResource):
    class Meta:
        limit = 0
        queryset = Service.objects.all()
        resource_name = 'service'
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        excludes = ['last_run']


class PodcastResource(ModelResource):

    service = fields.ForeignKey(ServiceResource, 'service', full=True)

    class Meta:
        limit = 0
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        queryset = Podcast.objects.all()
        resource_name = 'podcast'


class StoryResource(ModelResource):

    service = fields.ForeignKey(ServiceResource, 'service', full=True)

    class Meta:
        limit = 0
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        queryset = Story.objects.all()
        resource_name = 'story'

    def get_object_list(self, request):
        hours_ago_24 = maya.now().subtract(hours=48).datetime()
        return super(StoryResource, self).get_object_list(request).filter(story_date__gte=hours_ago_24)

    def dehydrate(self, bundle):
        # bundle.data['custom_field'] = "Whatever you want"
        if hasattr(bundle.obj, 'podcast'):
            podcast_res = PodcastResource()
            podcast_bundle = podcast_res.build_bundle(obj=bundle.obj.podcast, request=bundle.request)
            bundle.data = podcast_res.full_dehydrate(podcast_bundle).data
        return bundle


