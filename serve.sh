#!/bin/bash

# python manage.py db init
# python manage.py db migrate --message 'initial database migration'
# make migrate
# make run
python manage.py db upgrade
python manage.py test
python manage.py run