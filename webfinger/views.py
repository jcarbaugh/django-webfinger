from webfinger import Acct, XRDResponse, endpoint_hander

def endpoint(request, uri):
    acct = Acct(uri)
    response = XRDResponse(subject=acct)
    return endpoint_hander(acct, xrd)