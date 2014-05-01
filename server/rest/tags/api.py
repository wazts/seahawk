from tastypie.resources import ModelResource
from tags.models import Tag


class TagResource(ModelResource):
    class Meta:
        queryset = Tag.objects.all()
        resource_name = 'tag'