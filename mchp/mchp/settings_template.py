"""
Django settings for mchp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    'lib',
    'landing',
    'user_profile',
    'calendar_mchp',
    'documents',
    'dashboard',
    'referral',
    'schedule',
    'payment',

    'storages',
    'stored_messages',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.twitter',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'lib.middleware.UserMigrationMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'referral.middleware.ReferralMiddleware',
    'lib.middleware.TimezoneMiddleware',
    'lib.middleware.CustomMessageMiddleware',
)

from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {message_constants.ERROR: 'danger'}
MESSAGE_STORAGE = 'stored_messages.storage.PersistentStorage'

ROOT_URLCONF = 'mchp.urls'

WSGI_APPLICATION = 'mchp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
    }
}

import sys
if 'test' in sys.argv:
    SOUTH_TESTS_MIGRATE = False
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Phoenix'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# django-storages
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = 'mchp-dev'
#AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
# callingformat.subdomain is 2, let's hope this doesn't change
AWS_CALLING_FORMAT = 2

DEFAULT_FILE_STORAGE = 'documents.s3utils.MediaS3Storage' 
STATICFILES_STORAGE = 'documents.s3utils.StaticS3Storage'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '//{}.s3.amazonaws.com/static/'.format(AWS_STORAGE_BUCKET_NAME)
# STATIC_URL = '/static/'
STATIC_ROOT = '/static/'

MEDIA_URL =  '//{}.s3.amazonaws.com/media/'.format(AWS_STORAGE_BUCKET_NAME)
MEDIA_ROOT = '/media/'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.messages.context_processors.messages",
    # Required by allauth template tags
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    # allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)
LOGIN_REDIRECT_URL = '/dashboard/'
SOCIALACCOUNT_QUERY_EMAIL = True

# email
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'AKIAILBSJCVZ2FI3ZF7A'
EMAIL_HOST_PASSWORD = 'AkC6J6wQL474JQ2KRnPj3Yrbk1TgMOsb4m/wJoaMnx8P'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'contact@mycollegehomepage.com'

# Add this depending on the id of the site
#SITE_ID = 2

# import from allauth_settings.py
from mchp.allauth_settings import *

# 
# Stripe
#
STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY", "pk_test_trLdDuux3wpqI52nw0U3iNq3")
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "sk_test_ZnZ8MHHA3ECLS9JXJwBCE4pw")

# celery
# default RabbitMQ broker
BROKER_URL = 'amqp://'

# default RabbitMQ backend
CELERY_RESULT_BACKEND = 'amqp://'
from datetime import timedelta
CELERYBEAT_SCHEDULE = {
    'collect-subscriptions': {
        'task': 'calendar_mchp.tasks.bill_collector',
        'schedule': timedelta(hours=12),
    },
}
CELERY_TIMEZONE = 'UTC'

#Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR + '/mchp/debug.log',
        },
        'null': {
            'level': 'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        # # don't show all those sql statements
        # 'django.db.backends': {
        #     'handlers': ['null'],  # Quiet by default!
        #     'propagate': False,
        #     'level':'DEBUG',
        # },
    },
}
DEFAULT_HTTP_PROTOCOL = "https"
# site related pricing stuff
MCHP_PRICING = {
    # percent out of 100
    'commission_rate': 40,
    'subscription_length': timedelta(days=14),
    'delinquent_subscription_length': timedelta(days=1),
    'calendar_expiration': timedelta(days=183),
}


REF_GET_PARAMETER = 'ref'
REF_SESSION_KEY = 'referrer'
