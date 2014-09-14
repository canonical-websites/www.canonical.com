"""
Django settings for canonical project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Keep it secret, keep it safe!
SECRET_KEY = 'o@kjnphb9#+3fl80i#$v$+0la3u^atow)b33h*bafbcwir0w04'

# See https://docs.djangoproject.com/en/dev/ref/contrib/
INSTALLED_APPS = ['template_extensions']

ALLOWED_HOSTS = [
    '0.0.0.0', '127.0.0.1', 'localhost',
    '*.ubuntu.qa', '*.ubuntu.com', 'ubuntu.com'
]

MIDDLEWARE_CLASSES = []

ROOT_URLCONF = 'webapp.urls'
WSGI_APPLICATION = 'webapp.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = True
USE_TZ = True
STATIC_ROOT = "static"
STATIC_URL = '/static/'
TEMPLATE_DIRS = [os.path.join(BASE_DIR, "templates")]

# See http://tinyurl.com/django-context-processors
TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.static",  # Provides STATIC_URL
    "template_extensions.asset_server_url",  # {{ ASSET_SERVER_URL }}
]
