mchp-dev
========

Installation
------------

Clone the repository:
```
$ git clone https://github.com/mitchellias/mchp-dev
```
Install Python 3

Using homebrew:
```
$ brew install python3
```
Set up virtualenv:

Depending on your package manager and OS, the name of your virtual env may differ from below.

For Mac:
```
$ pyvenv3.4 /mchp-dev
$ source mchp-dev/bin/activate
```
Other:
```
$ virtualenv3 ./mchp-dev
$ source mchp-dev/bin/activate
```
Install psycopg2 and postgres

For Mac:
```
$ pip install psycopg2
$ brew install postgresql
```
In the repository, install django:
```
$ pip install -r requirements.txt
```

Copy the settings_template.py to settings.py and add local changes. The dev is responsible for keeping this up to date any time it changes.

Create the database, e.g. on the command line:
```$ createdb mchp```

Migrate the database: ```python manage.py migrate```

Create a superuser: ```python manage.py createsuperuser```

For getting AllAuth and Facebook integration working:
```
UPDATE django_site SET DOMAIN = '127.0.0.1:8000', name = 'mchp' WHERE id=1;
INSERT INTO socialaccount_socialapp (provider, name, secret, client_id, "key")
  VALUES ('facebook', 'Facebook', '--put-your-own-app-secret-here--', '--put-your-own-app-id-here--', '');
INSERT INTO socialaccount_socialapp_sites (socialapp_id, site_id) VALUES (1, 1);
```

Amazon access id and secret key are now taken from environmental variables. Put these commands in a .bashrc or similar file to have them run every time a new shell is started. The settings file will take care about loading these.
```
export AWS_ACCESS_KEY_ID=--your-access-key--
export AWS_SECRET_ACCESS_KEY=--your-secret-key--
```

For rabbitMQ (maybe):
```
# rabbitmq-server
```
For starting celery, make sure you are on the same level as manage.py (start rabbitMQ first):
```
# celery -A mchp worker -l info
```
