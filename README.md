mchp-dev
========

Installation
------------

Clone the repository:
```
$ git clone https://github.com/mitchellias/mchp-dev
```

Install Vagrant
* [http://www.vagrantup.com/downloads.html](http://www.vagrantup.com/downloads.html)

Start VM
```
vagrant up
```

Start the server
```
sh ./run_server.sh
```

Navigate to [http://localhost:8000](http://localhost:8000). You can log in with following credentials:
```
username: student
password: password
```

### Other useful comands
Django shell
```
sh ./run_shell.sh
```

Celery - used for uploading documents to S3. Using RabbitMQ as a broker, which is already installed in the VM.
```
sh ./run_celery.sh
```

Recreating environment
```
vagrant destroy
vagrant up
```

SSH into the VM for performing manual operations (i.e. installing new package, migrating the database etc.)
```
vagrant ssh
```

Stopping the server
```
sh ./stop_server.sh
```

Manual installation
------------
See ```vagrant/install.sh``` script that installs and sets up all dependencies.
