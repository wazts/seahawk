from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns ('tags.views',
url(r'^tags/$', 'tag_list'),
url(r'^tags/(?P<pk>[0-9]+)/$', 'tag_detail'),

)

urlpatterns = format_suffix_patterns (urlpatterns);