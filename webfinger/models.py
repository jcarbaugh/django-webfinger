from django.db import models
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from webfinger.rel import DESCRIBEDBY, WEBFINGER
import urllib
import wellknown

endpoint = urllib.unquote(reverse('webfinger_endpoint', args=(r'{uri}',)))
uri_template = "http://%s%s" % (Site.objects.get_current().domain, endpoint)

wellknown.get_hostmeta().register_link(
    rels=(DESCRIBEDBY, WEBFINGER),
    uri_template=uri_template,
    title='Resource Descriptor',
)