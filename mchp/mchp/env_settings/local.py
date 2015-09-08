import os
from .base import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yL6&8G%J9ihN*zNZUST5WIrtElZzlteL'
ALLOWED_HOSTS = []

INSTALLED_APPS += (
    'django_extensions',
    'debug_toolbar',
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mchp',
        'USER': 'mchp',
        'HOST': 'localhost',
        'PASSWORD': 'mchp_psql',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
    'rss_cache': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

import sys
if 'test' in sys.argv:
    SOUTH_TESTS_MIGRATE = False
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

# django-storages
AWS_ACCESS_KEY_ID = 'AKIAJO45NNRSGT2SPL5Q'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'mchp-dev'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
MEDIA_URL =  '//{}.s3.amazonaws.com/media/'.format(AWS_STORAGE_BUCKET_NAME)
DEFAULT_FILE_STORAGE = 'documents.s3utils.MediaS3Storage'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

COLLECTED_DIR = os.path.join(BASE_DIR, os.pardir, 'collected')
STATIC_ROOT = os.path.join(COLLECTED_DIR, 'static')
MEDIA_ROOT = os.path.join(COLLECTED_DIR, 'media')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Add this depending on the id of the site
SITE_ID = 1

#
# Stripe
#
STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY", "pk_test_trLdDuux3wpqI52nw0U3iNq3")
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "sk_test_ZnZ8MHHA3ECLS9JXJwBCE4pw")

#Logging
# LOGGING = {
#     'version': 1,
#     # 'disable_existing_loggers': True,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         }
#     },
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': BASE_DIR + '/mchp/debug.log',
#         },
#         'null': {
#             'level': 'DEBUG',
#             'class':'django.utils.log.NullHandler',
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler',
#             'include_html': True,
#             'email_backend': 'django_smtp_ssl.SSLEmailBackend',
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['null'],
#             'propagate': True,
#             'level': 'INFO',
#         },
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#     },
# }

# site related pricing stuff
MCHP_PRICING = {
    # percent out of 100
    'commission_rate': 40,
    'subscription_length': timedelta(days=14),
    'delinquent_subscription_length': timedelta(days=1),
    'calendar_expiration': timedelta(days=183),
    'referral_reward': 200,
}
