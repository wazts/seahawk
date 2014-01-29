from django.forms import widgets
from rest_framework import serializers
from tags.models import Tag

class TagSerializer (serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ('id', 'user', 'ip', 'major', 'minor')