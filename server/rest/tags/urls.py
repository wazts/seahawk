from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from tags import views

urlpatterns = patterns ('',
url(r'^tags/$', views.TagList.as_view()),
url(r'^tags/(?P<pk>[0-9]+)/$', views.TagDetail.as_view()),

)

urlpatterns = format_suffix_patterns (urlpatterns);