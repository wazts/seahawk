from django.conf.urls import patterns, url, include
from tags import views
from rest_framework.routers import DefaultRouter
from tags.api import TagResource
from tastypie.api import Api

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'tags', views.TagViewSet)
router.register(r'users', views.UserViewSet)

# tasty pie
v1_api = Api(api_name='v1')
v1_api.register(TagResource())

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
urlpatterns = patterns('',
	url(r'^api/', include (v1_api.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)