
"""
Django settings for role_initiative project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""



try:
	import pymysql
	pymysql.install_as_MySQLdb()
except ImportError:
	pass


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.core.urlresolvers import reverse
from django.contrib.messages import constants as messages
import requests


# Default context processors
import django.conf.global_settings as DEFAULT_SETTINGS
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP, LOGGING

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['10.0.0.34']


AUTH_USER_MODEL = 'auth.User'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

here = lambda *path: os.path.normpath(os.path.join(os.path.dirname(__file__), *path))
ROOT = lambda *path: here("../../", *path)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Files
MAX_UPLOAD_SIZE = 50 * 2**20
CHUNK_SIZE = 1 * 2**20
ITEMS_PER_PAGE = 10


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pytz',
    'south',
    'role_initiative.home',
    'role_initiative.featured_games',
    'role_initiative.users',
    'role_initiative.files',
    'role_initiative.games',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

)

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)


ROOT_URLCONF = 'role_initiative.urls'

WSGI_APPLICATION = 'role_initiative.wsgi.application'



# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
	here("../", "static"),
)
STATIC_ROOT = ROOT("static")

MEDIA_ROOT = ROOT("media")
MEDIA_URL = '/media/'

TMP_ROOT = ROOT("tmp")

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_DIRS = (
   	here('../', "templates"),
)

