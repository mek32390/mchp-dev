mchp-dev
========

Installation
------------

Clone the repository:
```
$ git clone https://github.com/mitchellias/mchp-dev
```
Set up virtualenv: 
```
$ virtualenv3 ./mchp-dev
$ source mchp-dev/bin/activate
```
In the repository, install django:
```
$ pip install -r requirements.txt
```
Copy the settings_template.py to settings.py and add local changes. The dev is responsible for keeping this up to date any time it changes.

For getting AllAuth and Facebook integration working:
```
UPDATE django_site SET DOMAIN = '127.0.0.1:8000', name = 'mchp' WHERE id=2;
INSERT INTO socialaccount_socialapp (provider, name, secret, client_id, `key`)
VALUES ("facebook", "Facebook", "--put-your-own-app-secret-here--", "--put-your-own-app-id-here--", '');
INSERT INTO socialaccount_socialapp_sites (socialapp_id, site_id) VALUES (1,2);
```
And then set up the facebook side as well.

To use south with already existing development environments:
```
pip install -r requirements.txt
./manage syncdb
./manage migrate --fake
```

For new developers run:
```
./manage migrate 
```
without the --fake argument.
