from django.db import models
from django.contrib.auth.models import User

class Tag (models.Model):

	created = models.DateTimeField (auto_now_add=True)
	user = models.ForeignKey (User)
	ip = models.GenericIPAddressField ()
	major = models.PositiveIntegerField()
	minor = models.PositiveIntegerField()

	class Meta:
		ordering = ('created',)