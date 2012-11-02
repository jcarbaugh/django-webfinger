from django.conf import settings
from django.utils.importlib import import_module
import webfinger

handler_path = getattr(settings, 'WEBFINGER_HANDLER', None)
if handler_path is None:
    raise ValueError('setting WEBFINGER_HANDLER is required')
handler_path = handler_path.encode('ascii')
(mod_name, func_name) = handler_path.rsplit('.', 1)

HANDLER = getattr(import_module(mod_name), func_name)

def endpoint(request, uri):
    acct = webfinger.Acct(uri)
    response = webfinger.XRDResponse(subject=acct)
    HANDLER(request, acct, response._xrd)
    return response
