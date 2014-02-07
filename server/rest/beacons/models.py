from django.db import models
from django.contrib.auth.models import User
from uuidfield import UUIDField

class Beacon (models.Model):
	"""
	The beacons that we can tag. 
	"""
	time_created = models.DateTimeField (auto_now_add=True)
	user = models.ForeignKey (User, related_name='beacons', blank=True)
	uuid = UUIDField(auto=True)
	major = models.PositiveIntegerField()
	minor = models.PositiveIntegerField()

	class Meta:
		ordering = ('time_created',)