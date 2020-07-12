#!/bin/bash

service rabbitmq-server start
/etc/init.d/mysql start
cd /opt/app/src/
celery -A monitor worker -l info -n worker &
celery -A monitor beat -l INFO &
python manage.py migrate --no-input
python manage.py runserver 0.0.0.0:8000