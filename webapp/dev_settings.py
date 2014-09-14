from settings import *

INSTALLED_APPS += ('django_extensions',)
TEMPLATE_DEBUG = True
DEBUG = True

# For some reason, django.contrib.staticfiles.views.serve()
# doesn't work with only STATIC_ROOT set,
# even though it's supposed to
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATICFILES_DIRS = [os.path.join(BASE_DIR, STATIC_ROOT)]
STATIC_ROOT = ''
