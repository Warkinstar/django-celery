# Asynchronous Tasks with Django and Celery

Example of how to handle background processes with Django, Celery, and Docker.

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/django-and-celery/).

## Want to use this project?

Spin up the containers:

```sh
$ docker-compose up -d --build
```

Open your browser to http://localhost:8000 to view the app or to http://localhost:5555 to view the Flower dashboard.

Trigger a new task:

```sh
$ curl -F type=0 http://localhost:8000/tasks/
```

Check the status:

```sh
$ curl http://localhost:8000/tasks/<TASK_ID>/
```

# Handling Periodic Tasks in Django with Celery and Docker

Example of how to manage periodic tasks with Django, Celery, and Docker

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/django-celery-periodic-tasks/).

## Want to use this project?

Spin up the containers:

```sh
$ docker-compose up -d --build
```

Open the logs associated with the `celery` service to see the tasks running periodically:

```sh
$ docker-compose logs -f 'celery'
```
