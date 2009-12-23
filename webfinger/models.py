from django.db import models
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from webfinger.rel import DESCRIBEDBY
from xrd import Link
import urllib
import wellknown

endpoint = urllib.unquote(reverse('webfinger_endpoint', args=(r'{uri}',)))
uri_template = "http://%s%s" % (Site.objects.get_current().domain, endpoint)

webfinger_link = Link(rel=DESCRIBEDBY, template=uri_template)
webfinger_link.titles.append('Resource Descriptor')

wellknown.get_hostmeta().links.append(webfinger_link)