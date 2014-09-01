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

INSTALLED_APPS = (
    'django.contrib.staticfiles',  # Needed for STATIC_URL to work
)

ROOT_URLCONF = 'canonical.urls'
WSGI_APPLICATION = 'canonical.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
TEMPLATE_DIRS = (BASE_DIR + "/templates")
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(TEMPLATE_DIRS, "static"), )
