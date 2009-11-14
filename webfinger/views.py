from django.conf import settings
from django.utils.importlib import import_module
import webfinger

pretty = getattr(settings, 'WEBFINGER_PRETTY', False)
handler_path = getattr(settings, 'WEBFINGER_HANDLER', None)

if handler_path is None:
    raise ValueError('setting WEBFINGER_HANDLER is required')
    
handler_path = handler_path.encode('ascii')

(mod_name, func_name) = handler_path.rsplit('.', 1)

HANDLER = getattr(import_module(mod_name), func_name)

def endpoint(request, uri):
    acct = webfinger.Acct(uri)
    xrd = webfinger.XRDResponse(subject=acct, pretty=pretty)
    HANDLER(acct, xrd)
    return xrd