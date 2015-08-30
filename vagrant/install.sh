#!/bin/bash

# Script to set up dependencies for Django on Vagrant.

# Install essential packages from Apt
sudo apt-get update -y
sudo apt-get install language-pack-en
sudo apt-get install -y git
sudo apt-get install -y libmagickwand-dev

# Postgresql
if ! command -v psql; then
  sudo apt-get install -y postgresql-9.3 postgresql-server-dev-9.3
  sudo /etc/init.d/postgresql reload

  cat << EOF | sudo -u postgres psql
  -- Create the database user:
  CREATE USER mchp WITH PASSWORD 'mchp_psql';

  -- Create the database:
  CREATE DATABASE mchp WITH OWNER mchp;
EOF
fi

# Fixing Ubuntu 14 pyvenv bug
# http://askubuntu.com/questions/488529/pyvenv-3-4-error-returned-non-zero-exit-status-1
sudo apt-get install -y python3-pip
sudo pip3 install virtualenv

# Installing RabbitMQ for celery
sudo apt-get install -y rabbitmq-server

# Setting up environment
virtualenv /home/vagrant/mchp-dev
sudo chown -R vagrant /home/vagrant/mchp-dev
source /home/vagrant/mchp-dev/bin/activate
pip install -r /vagrant/requirements.txt
pip install -r /vagrant/local_requirements.txt
cd /vagrant/mchp/

python manage.py migrate

echo "
school = School.objects.create(domain='mchpteam.edu', name='mchp school')
user = User.objects.create_superuser('mchp', 'mchp@mchpteam.edu', 'mchp_password')
Student.objects.create_student(user, school)
user = User.objects.create_superuser('student', 'student@mchpteam.edu', 'password')
Student.objects.create_student(user, school)
EmailAddress.objects.create(user=user, email=user.email, verified=True, primary=True)
" | python manage.py shell_plus

FACEBOOK_APP_ID=1615168388737533
FACEBOOK_SECRET=65668459ca09d478c021d20cacfd3e41

sudo -u postgres psql -d mchp -c "
    UPDATE django_site SET DOMAIN = '127.0.0.1:8000', name = 'mchp' WHERE id=1;
    INSERT INTO socialaccount_socialapp (provider, name, secret, client_id, "key")
      VALUES ('facebook', 'Facebook', '$FACEBOOK_SECRET', '$FACEBOOK_APP_ID', '');
    INSERT INTO socialaccount_socialapp_sites (socialapp_id, site_id) VALUES (1, 1);
"
