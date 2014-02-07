from django.db import models
from django.contrib.auth.models import User
from beacons.models import Beacon

class Tag (models.Model):

	time_created = models.DateTimeField (auto_now_add=True)
	user = models.ForeignKey (User, related_name='tags')
	beacon_tagged = models.ForeignKey (Beacon, related_name='beacons', blank=True)
	ip = models.GenericIPAddressField ()
	some = models.CharField(max_length=10, default="")

	class Meta:
		ordering = ('time_created',)