======================================
Django Redirect Middleware
======================================

Quick Start
```````````

Add ``django.contrib.redirects`` to INSTALLED_APPS ::
    
    INSTALLED_APPS = [
        ...
	    'django.contrib.redirects',
        ...
    ]

Add ``redirects.middleware.RedirectMiddleware`` to MIDDLEWARE_CLASSES ::

	MIDDLEWARE_CLASSES = [
		...
		'redirects.middleware.RedirectMiddleware',
		...
	]

Synchronize your database models run ``django syncdb``
