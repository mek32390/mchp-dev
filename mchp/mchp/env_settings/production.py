import os
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ADMINS = (
    ('mitch', 'ekemekm@gmail.com'),
)

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    'www.mycollegehomepage.com',
    'www.mycollegehomepage.com.',
    'mycollegehomepage.com',
    'mycollegehomepage.com',
]

CACHES = {
    # not used
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'default_cache',
    },
    'rss_cache': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'rss_cache',
    }
}

# django-storages
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = 'mchp-production'
#AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
# callingformat.subdomain is 2, let's hope this doesn't change
AWS_S3_SECURE_URLS = True

DEFAULT_FILE_STORAGE = 'documents.s3utils.MediaS3Storage'
STATICFILES_STORAGE = 'documents.s3utils.StaticS3Storage'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = 'https://{}.s3.amazonaws.com/static/'.format(AWS_STORAGE_BUCKET_NAME)
STATIC_ROOT = '/static/'

MEDIA_URL =  'https://{}.s3.amazonaws.com/media/'.format(AWS_STORAGE_BUCKET_NAME)
MEDIA_ROOT = '/media/'

# email
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'AKIAILBSJCVZ2FI3ZF7A'
EMAIL_HOST_PASSWORD = 'AkC6J6wQL474JQ2KRnPj3Yrbk1TgMOsb4m/wJoaMnx8P'
EMAIL_USE_TLS = True
SERVER_EMAIL = 'mchp error <contact@mycollegehomepage.com>'
DEFAULT_FROM_EMAIL = 'mchp contact <contact@mycollegehomepage.com>'

# Add this depending on the id of the site
SITE_ID = 3


#Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
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
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
            'email_backend': 'django_smtp_ssl.SSLEmailBackend',
        },
        'celery': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'celery.log',
            'maxBytes': 1024 * 1024 * 100,  # 100 mb
        },
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'celery.task': {
            'handlers': ['celery'],
            'level': 'ERROR',
        },
    },
}
# site related pricing stuff
MCHP_PRICING = {
    # percent out of 100
    'commission_rate': 40,
    'subscription_length': timedelta(days=14),
    'delinquent_subscription_length': timedelta(days=1),
    'calendar_expiration': timedelta(days=183),
    'referral_reward': 200,
}


# TODO Set up sensitive data

# Stripe
STRIPE_PUBLIC_KEY = ''
STRIPE_SECRET_KEY = ''

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}