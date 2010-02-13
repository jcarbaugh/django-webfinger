from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from webfinger.rel import LRDD
from xrd import Link
import urllib
import wellknown

SECURE = getattr(settings, 'WEBFINGER_SECURE', False)
scheme = "https" if SECURE else "http"

endpoint = urllib.unquote(reverse('webfinger_endpoint', args=(r'{uri}',)))
uri_template = "%s://%s%s" % (scheme, Site.objects.get_current().domain, endpoint)

webfinger_link = Link(rel=LRDD, template=uri_template)
webfinger_link.titles.append('Resource Descriptor')

wellknown.get_hostmeta().links.append(webfinger_link)