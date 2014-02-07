from django.forms import widgets
from rest_framework import serializers
from tags.models import Tag, Beacon
from django.contrib.auth.models import User

class TagSerializer (serializers.HyperlinkedModelSerializer):
	user = serializers.Field (source='user.username')
	class Meta:
		model = Tag
		fields = ('url', 'time_created','user', 'ip', 'beacon_tagged')

class UserSerializer (serializers.HyperlinkedModelSerializer):
	tags = serializers.HyperlinkedRelatedField(many=True, view_name='tag-detail')

	class Meta:
		model = User
		fields = ('url', 'username', 'tags')