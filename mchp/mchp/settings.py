import os

environment = os.environ.get('ENVIRONMENT', '')

print('ENVIRONMENT: ' + environment)

if environment == 'production':
    from .env_settings.production import *
elif environment == 'staging':
    from .env_settings.staging import *
else:
    from .env_settings.local import *
