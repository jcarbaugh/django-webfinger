Initial version... needs some major refactoring

================
django-webfinger
================

Provide webfinger service.

Requirements
============

python >= 2.5

django >= 1.0

django-wellknown

Installation
============

Be sure to add ``webfinger`` to ``INSTALLED_APPS`` in settings.py. Additionally, add the following entry to urls.py::

	urls(r'^webfinger/', include('webfinger.urls')),

And later in urls.py::

	import webfinger
	webfinger.init()

The plan is to get rid of the ``init()`` call, but I need to put more effort into it.

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
	    xrd.add_alias('http://example.com/profile/%s/' % acct.userinfo)
	    xrd.set_expires(datetime.datetime.utcnow() + datetime.timedelta(0, 10))
	    xrd.register_link(
	        rels=(rel.AUTHOR, rel.HCARD, rel.PROFILE),
	        uri='http://jeremy.carbauja.com',
	        titles='this is me!',
	        media_type='text/html',
	    )
