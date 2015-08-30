vagrant ssh -- "sudo killall python;\
source /home/vagrant/mchp-dev/bin/activate && \
cd /vagrant/mchp && \
python manage.py runserver_plus 0.0.0.0:8000"
