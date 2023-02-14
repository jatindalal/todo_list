# Todo List

This is a todo list application created using Django and bootstrap

[https://todo-list-12dx.onrender.com](https://todo-list-12dx.onrender.com)

## Setup

![screenshot](images/screenshot.png)

### Docker
You can use the pre-built image and create an image from scratch. The service runs of port 80 inside the container, so make sure to expose it while creating the container.

```
docker run -it --rm -p 80:80 thassiboy/todo_list
```

### Local
To run the app locally you need to setup the DJANGO_SECRET environment variable and install all the requirements. It is recommended that you use a virtual environment.

```
pip install -r requirements.txt

echo DJANGO_SECRET=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())') >> .env

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
