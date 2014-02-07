from beacons.models import Beacon
from beacons.serializers import BeaconSerializer
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


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'beacons': reverse('beacon-list', request=request, format=format)
    })


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