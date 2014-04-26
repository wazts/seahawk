from django.conf.urls import patterns, url, include
from beacons import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'beacons', views.BeaconViewSet)
router.register(r'btbeacons', views.BTBeaconViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)