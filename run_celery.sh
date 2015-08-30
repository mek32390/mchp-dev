vagrant ssh -- "source /home/vagrant/mchp-dev/bin/activate && \
cd /vagrant/mchp && \
celery -A mchp worker -l info"
