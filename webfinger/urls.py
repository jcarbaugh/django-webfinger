from django.conf.urls.defaults import *

urlpatterns = patterns('webfinger.views',
    url(r'^(?P<uri>.+)/$', 'endpoint', name='webfinger_endpoint'),
)