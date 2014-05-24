from django.db import models
from django.contrib.auth.models import User

class Beacon (models.Model):
	"""
	The beacons that we can tag. 
	"""

	user = models.ForeignKey (User, related_name='beacons', blank=False)
	time_created = models.DateTimeField (auto_now_add=True)

	class Meta:
		ordering = ('time_created',)

	def __unicode__(self):
		return self.pk

class AreaBeacon (Beacon):
	"""
		The Area beacon is used for tagging when a user doesn't have 
		Bluetooth 4.0
	"""
	latitude = models.FloatField ()
	longitude = models.FloatField ()

class BluetoothBeacon (Beacon):
	"""
		The traditional iBeacon
	"""
	uuid = models.CharField (max_length=32)
	major_id = models.IntegerField ()
	minor_id = models.IntegerField ()

