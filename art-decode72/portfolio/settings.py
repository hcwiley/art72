# Django settings for portfolio project.

import sys
import os
import posixpath

import socket


sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir)))

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

host = socket.gethostname()
IS_DEV = host in ('blu-wired', 'lil-italy') 
DEBUG = True

if IS_DEV:
    DATABASE_ENGINE = 'django.db.backends.sqlite3'
    DATABASE_NAME = 'art72.db'
    DATABASE_USER = ''
    DATABASE_PASSWORD = ''
MEDIA_ROOT = PROJECT_ROOT.replace('portfolio','site_media/media')
STATIC_DOC_ROOT = MEDIA_ROOT
GALLERY_ROOT = os.path.join(MEDIA_ROOT, 'gallery')
THUMB_ROOT = os.path.join(GALLERY_ROOT, "thumbs")
MEDIA_URL = 'site_media/media/'
STATIC_URL = "site_media/static/"
GALLERY_URL = "site_media/media/gallery/"
THUMB_URL = "site_media/media/gallery/thumbs/"
ADMIN_MEDIA_PREFIX = "%s/admin/" % MEDIA_URL

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
    'artist',
    'contact_element',
)
try:
    from local_settings import *
except ImportError:
    pass
