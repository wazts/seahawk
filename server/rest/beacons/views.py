from beacons.models import *
from beacons.serializers import BeaconSerializer, BTBeaconSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from beacons.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.decorators import link

from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class BeaconViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Beacon.objects.all()
    serializer_class = BeaconSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

class BTBeaconViewSet (viewsets.ModelViewSet):
    queryset = BluetoothBeacon.objects.all()
    serializer_class = BTBeaconSerializer

    def pre_save(self, obj):
        obj.user = self.request.user