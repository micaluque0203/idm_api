#!/bin/bash

python --version
export PYTHONPATH=/var/www/

python /var/www/application.py db upgrade
python /var/www/application.py runserver --host 0.0.0.0 --port 80 -d