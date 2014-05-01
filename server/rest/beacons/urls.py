from django.conf.urls import patterns, url, include
from beacons import views
from rest_framework.routers import DefaultRouter
from tastypie.api import Api
from beacons.api import BeaconResource
from beacons.api import UserResource

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'beacons', views.BeaconViewSet)
router.register(r'btbeacons', views.BTBeaconViewSet)

# Tasty Pie
v1_api = Api (api_name='v1')
v1_api.register(BeaconResource())
v1_api.register(UserResource())

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api/', include(v1_api.urls))
)