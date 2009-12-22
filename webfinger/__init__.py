from django.http import HttpResponse
from django.template.loader import render_to_string
from xml.dom.minidom import parseString
from xrd import XRD
import re

endpoint_hander = None

ACCT_RE = re.compile(r'(?:acct:)?(?P<userinfo>[\w.!#$%&\'*+-/=?^_`{|}~]+)@(?P<host>[\w.:-]+)')

def _force_list(v):
    if v is not None:
        if isinstance(v, (list, tuple)):
            return v
        return [v]

class Acct(object):
    def __init__(self, acct):
        m = ACCT_RE.match(acct)
        if not m:
            raise ValueError('invalid acct format')
        (userinfo, host) = m.groups()
        self.userinfo = userinfo
        self.host = host
    def __unicode__(self):
        return u"acct:%s@%s" % (self.userinfo, self.host)

class XRDResponse(HttpResponse):

    def __init__(self, subject=None, **kwargs):
        from django.conf import settings
        content_type = 'text/plain' if settings.DEBUG else 'application/xrd+xml'
        super(XRDResponse, self).__init__(content_type=content_type, **kwargs)
        self.xrd = XRD()

    def __iter__(self):
        content = render_to_string('webfinger/xrd.xml', self.xrd.to_xml())
        self._iterator = iter((content),)
        return self
