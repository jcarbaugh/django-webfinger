from django.conf import settings
from django.core.urlresolvers import reverse

from webfinger.rel import LRDD
from xrd import Link

import urllib
import wellknown

SECURE = getattr(settings, 'WEBFINGER_SECURE', False)
DOMAIN = getattr(settings, 'WEBFINGER_DOMAIN', 'example.com')

scheme = "https" if SECURE else "http"

endpoint = urllib.unquote(reverse('webfinger_endpoint', args=(r'{uri}',)))
uri_template = "%s://%s%s" % (scheme, DOMAIN, endpoint)

webfinger_link = Link(rel=LRDD, template=uri_template)
webfinger_link.titles.append('Resource Descriptor')

wellknown.get_hostmeta().links.append(webfinger_link)
