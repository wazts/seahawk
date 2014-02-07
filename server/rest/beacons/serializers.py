from django.forms import widgets
from rest_framework import serializers
from beacons.models import Beacon
from django.contrib.auth.models import User

class BeaconSerializer (serializers.HyperlinkedModelSerializer):
	tags = serializers.HyperlinkedRelatedField(many=True, view_name='tag-detail')

	class Meta:
		model = Beacon
		fields = ('url', 'time_created', 'user', 'uuid', 'major', 'minor')