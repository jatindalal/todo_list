FROM python:3.10

WORKDIR /app
COPY . /app
RUN chown -R www-data:www-data /app

RUN pip install -r requirements.txt --no-cache-dir
RUN echo DJANGO_SECRET=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())') >> .env

EXPOSE 80
CMD [ "gunicorn", "todo_list.wsgi", "--user", "www-data", "--bind", "0.0.0.0:80", "--workers", "3" ]