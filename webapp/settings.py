"""
Django settings for canonical project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# See https://docs.djangoproject.com/en/dev/ref/contrib/
INSTALLED_APPS = [
    'canonicalwebteam',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
]

SECRET_KEY = os.environ.get('SECRET_KEY', 'no_secret')
DEBUG = os.environ.get('DJANGO_DEBUG', 'false').lower() == 'true'

ALLOWED_HOSTS = ['*']

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

MIDDLEWARE_CLASSES = []

WHITENOISE_MAX_AGE = 31557600
WHITENOISE_ALLOW_ALL_ORIGINS = False

ROOT_URLCONF = 'webapp.urls'
WSGI_APPLICATION = 'webapp.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = True
USE_TZ = True
STATIC_ROOT = 'static'
STATIC_URL = '/static/'
STATICFILES_FINDERS = ['django_static_root_finder.StaticRootFinder']
ASSET_SERVER_URL = 'https://assets.ubuntu.com/v1/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'builtins': [
                'canonicalwebteam.get_feeds.templatetags',
            ],
            'context_processors': [
                'django.template.context_processors.static',
                'django_asset_server_url.asset_server_url',
            ],
        },
    },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'error_file': {
            'level': 'WARNING',
            'filename': os.path.join(BASE_DIR, 'django-error.log'),
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1 * 1024 * 1024,
            'backupCount': 2
        }
    },
    'loggers': {
        'django': {
            'handlers': ['error_file'],
            'level': 'WARNING',
            'propagate': True
        }
    }
}
