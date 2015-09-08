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
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'mchp/templates/'),)

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

    'demo',
    'lib',
    'landing',
    'user_profile',
    'calendar_mchp',
    'campaigns',
    'documents',
    'dashboard',
    'notification',
    'referral',
    'schedule',
    'studyguides',
    'payment',
    'rosters',

    'storages',

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
    'donottrack.middleware.DoNotTrackMiddleware',
)

from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {message_constants.ERROR: 'danger'}
INBOX_EXPIRE_DAYS = 30

ROOT_URLCONF = 'mchp.urls'

WSGI_APPLICATION = 'mchp.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Phoenix'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AWS_CALLING_FORMAT = 2

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.messages.context_processors.messages",
    # Required by allauth template tags
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    # allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
    "donottrack.context_processors.donottrack",
    "schedule.context_processors.school",
    "mchp.context_processors.max_images",
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)
LOGIN_REDIRECT_URL = '/home/'
SOCIALACCOUNT_QUERY_EMAIL = True


# import from allauth_settings.py
from mchp.allauth_settings import *

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

ADMIN_USERNAME = 'mchp'

REF_GET_PARAMETER = 'ref'
REF_SESSION_KEY = 'referrer'
