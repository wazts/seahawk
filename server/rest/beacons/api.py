from tastypie.resources import ModelResource
from beacons.models import Beacon, BluetoothBeacon
from django.contrib.auth.models import User
from tastypie import fields


class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		fields = ['username', 'first_name', 'last_name', 'last_login']

class BeaconResource(ModelResource):
	user = fields.ForeignKey (UserResource, 'user')

	def dehydrate(self, bundle):
		child = None

		try:
			child = bundle.obj.bluetoothbeacon
			bundle.data['major_id'] = child.major_id;
			bundle.data['minor_id'] = child.minor_id;
		except Exception:
			pass

		try:
			child = bundle.obj.areabeacon
			bundle.data['latitude'] = child.latitude;
			bundle.data['longitude'] = child.longitude;	
		except Exception:
			pass
			
		return bundle

	class Meta:
		queryset = Beacon.objects.all()
		resource_name = 'beacon'
		fields = ['user', 'time_created']