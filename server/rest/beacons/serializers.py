from django.forms import widgets
from rest_framework import serializers
from beacons.models import Beacon, BluetoothBeacon
from django.contrib.auth.models import User

class BeaconObjectRelatedField(serializers.RelatedField):
    """
    A custom field to use for the `beacon_object` generic relationship.
    """

    def to_native(self, value):
        """
        Serialize tagged objects to a simple textual representation.
        """                            
        if isinstance(value, BluetoothBeacon):
            serializer = BTBeaconSerializer
        else:
        	raise Exception('Unexpected type of beacon object')
        return serializer.data

class BeaconSerializer (serializers.HyperlinkedModelSerializer):
	beacon_type = BeaconObjectRelatedField (many=False)

	class Meta:
		model = Beacon
		fields = ('time_created', 'user')

class BTBeaconSerializer (serializers.HyperlinkedModelSerializer):
	beacons = serializers.HyperlinkedRelatedField (many=False, view_name='beacon-detail')

	class Meta:
		model = BluetoothBeacon
		fields = ('uuid', 'major_id', 'minor_id')