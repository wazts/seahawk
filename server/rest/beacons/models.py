from django.db import models
from django.contrib.auth.models import User

class Beacon (models.Model):
	"""
	The beacons that we can tag. 
	"""
	time_created = models.DateTimeField (auto_now_add=True)
	user = models.ForeignKey (User, related_name='beacons', blank=True)
	uuid = models.CharField (max_length=32, unique=False)
	major = models.PositiveIntegerField()
	minor = models.PositiveIntegerField()

	class Meta:
		ordering = ('time_created',)