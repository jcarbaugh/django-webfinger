Initial version... needs some major refactoring

================
django-webfinger
================

Provide webfinger service.

http://code.google.com/p/webfinger/wiki/WebFingerProtocol

Requirements
============

python >= 2.5

python-xrd

django >= 1.0

django-wellknown

Installation
============

Be sure to add ``webfinger`` to ``INSTALLED_APPS`` in settings.py. Additionally, add the following entry to urls.py::

	urls(r'^webfinger/', include('webfinger.urls')),

Configure the webfinger handler in settings.py::

	WEBFINGER_HANDLER = 'path.to.handler.func'

Usage
=====

Handler Function
----------------

::

	from webfinger import rel
	import datetime
	
	def handler_func(acct, xrd):
		# acct.userinfo is the username
		# acct.host is the host
	    xrd.aliases.append('http://example.com/profile/%s/' % acct.userinfo)
	    xrd.expires = datetime.datetime.utcnow() + datetime.timedelta(0, 10)
	    xrd.links.append(Link(
	        rel=rel.AUTHOR,
	        href='http://jeremy.carbauja.com',
	        type='text/html',
	    ))
