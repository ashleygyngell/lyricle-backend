#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt
pip install --upgrade pip
pip install --force-reinstall -U setuptools
pip install django
python manage.py collectstatic --no-input
python manage.py migrate
