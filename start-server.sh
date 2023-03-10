#!/usr/bin/env bash

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (python manage.py createsuperuser --no-input)
fi
(gunicorn todo_list.wsgi --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"