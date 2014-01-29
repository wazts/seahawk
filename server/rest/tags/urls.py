from django.conf.urls import patterns, url

urlpatterns = patterns ('tags.views',
url(r'^tags/$', 'tag_list'),
url(r'^tags/(?P<pk>[0-9]+)/$', 'tag_detail'),

)