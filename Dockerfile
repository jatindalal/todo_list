FROM python:3.10-buster

RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt --no-cache-dir

RUN python manage.py makemigrations
RUN python manage.py migrate

RUN echo DJANGO_SECRET=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())') >> .env

EXPOSE 80
CMD ["/app/start-server.sh"]