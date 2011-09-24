# Django settings for portfolio project.

import sys
import os
import posixpath

import socket

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
]

host = socket.gethostname()
IS_DEV = host in ('blu-wired', 'blu-Ubuntu',) # RIP 'lil-italy') 
IS_DEV = IS_DEV or 'Users' in os.listdir('/')
DEBUG = True

if IS_DEV:
    DATABASE_ENGINE = 'django.db.backends.sqlite3'
    DATABASE_NAME = 'art72.db'
    DATABASE_USER = ''
    DATABASE_PASSWORD = ''

    MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'user-media')
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'collected-static')
else:
    # set up email
    pass

GALLERY_ROOT = os.path.join(MEDIA_ROOT, 'gallery')
print os.listdir(GALLERY_ROOT)
#THUMB_ROOT = os.path.join(GALLERY_ROOT, 'thumbs/')
#
#if not os.path.exists(THUMB_ROOT):
#    os.makedirs(THUMB_ROOT)
GALLERY_URL = '/site_media/media/gallery/'
#THUMB_URL = '/site_media/media/gallery/thumbs/'
MEDIA_URL = '/site_media/media/'
STATIC_URL = '/site_media/static/'

STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]
ADMIN_MEDIA_PREFIX = os.path.join(STATIC_URL, 'admin/') 

sys.path.append(PROJECT_ROOT)
sys.path.append('%s/apps/' % PROJECT_ROOT)
sys.path.append('%s/apps/piece/' % PROJECT_ROOT)
sys.path.append('%s/apps/artist/' % PROJECT_ROOT)
sys.path.append('%s/apps/contact_element/' % PROJECT_ROOT)

FORCE_LOWERCASE_TAGS = True #for django-tagging
TEMPLATE_DEBUG = DEBUG
ADMINS = (
    ('Cole Wiley', 'hcwiley@gmail.com'),
    ('Zack Dever', 'zack@decode72.com'),
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
    'django.contrib.staticfiles',
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
