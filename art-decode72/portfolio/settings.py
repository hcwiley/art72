# Django settings for portfolio project.

import sys
import os
import posixpath

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir)))

IS_DEV = True
DEBUG = True

DATABASE_ENGINE = 'django.db.backends.mysql'
DATABASE_NAME = 'wd40too_artist'
DATABASE_USER = 'wd40too_artist'
DATABASE_PASSWORD = 'geaux44'

MEDIA_ROOT = (os.getcwd()+'').replace('portfolio','site_media/media/')
print MEDIA_ROOT
STATIC_DOC_ROOT = MEDIA_ROOT
GALLERY_ROOT = (os.getcwd()+'').replace('portfolio','site_media/media/gallery/')
MEDIA_URL = '/media/'
STATIC_URL = "/static/"
ADMIN_MEDIA_PREFIX = posixpath.join(MEDIA_URL, "admin/")

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
]

sys.path.append('./apps/')

FORCE_LOWERCASE_TAGS = True #for django-tagging
TEMPLATE_DEBUG = DEBUG
ADMINS = (
    ('Cole Wiley', 'hcwiley@gmail.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'mt&+05kny@@(r7c&re52_1cnb@$9goyrnar&+@fgi)xip=mi+n'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'portfolio.urls'
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'piece',
)
try:
    from local_settings import *
except ImportError:
    pass
