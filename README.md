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

For Mac:
```
$ pyenv3.4 /mchp-dev
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

For getting AllAuth and Facebook integration working:
```
UPDATE django_site SET DOMAIN = '127.0.0.1:8000', name = 'mchp' WHERE id=1;
INSERT INTO socialaccount_socialapp (provider, name, secret, client_id, "key")
  VALUES ('facebook', 'Facebook', '--put-your-own-app-secret-here--', '--put-your-own-app-id-here--', '');
INSERT INTO socialaccount_socialapp_sites (socialapp_id, site_id) VALUES (1,2);
```
And then set up the facebook social application via the admin as well.

To start elasticsearch:
```
# elasticsearch -d es.config=/path/to/elasticsearch.yml
```

Amazon access id and secret key are now taken from environmental variables. Put these commands in a .bashrc or similar file to have them run every time a new shell is started. The settings file will take care about loading these.
```
export AWS_ACCESS_KEY_ID=--your-access-key--
export AWS_SECRET_ACCESS_KEY=--your-secret-key--
```

pip install django-storages leaves out S3.py, so you'll need to make the file yourself in the “backends” folder where (lowercase) s3.py is also located.
Note: The file reference below is a recent change and these directions are going to change again soon! The django-storages project has a lot of improvements which have not yet been packaged, so keep watching this space.
If you are on a mac, it will not let you create a file named S3.py since there is already a file named s3.py. Change the name of the new S3.py file to S31.py, then on line 13 of s3.py, change the imported file name to S31.py
```
Here are the contents of that file: https://raw.githubusercontent.com/coagulant/django-storages-py3/py3/storages/utils/S3.py
```
For rabbitMQ (maybe):
```
# rabbitmq-server
```
For starting celery, make sure you are on the same level as manage.py (start rabbitMQ first):
```
# celery -A mchp worker -l info
```
