# DjangoFileAPI

## Функционал:

- загрузка, хранение, просмотр сохраненных файлов посредством API
- асинхронная обработка файлов с использованием celery

Проект "боевой" (готов к деплою) требуется:
- клонировать проект:
```sh
git clone https://github.com/demetrzz/djangofileapi
```
- создать файл .env в корне проекта по примеру, добавить домен/ip вашего сервера в ALLOWED_HOSTS:
```sh
DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_DB=db
DB_NAME=djangofileapi
DB_USER=postgres
DB_PASSWORD=testpassword
DB_PORT=5432
DEBUG=False
ALLOWED_HOSTS=0.0.0.0 127.0.0.1 localhost [::1]
SECRET_KEY=your_key_here
```
- настроить и запустить контейнеры docker:
```sh
docker compose build
docker compose up
```
- создать базу данных в контейнере:
```sh
docker exec -it container_id psql -U my_user
create database djangofileapi;
```

## Стек технологий

- Django
- DjangoRestFramework
- Python
- PostgreSQL
- Redis
- Celery

## Стек деплоя:

- Docker
- Gunicorn
- Nginx

## Проект задеплоен на Ubuntu 22.04:
http://94.228.121.80/api/files/

## TODO:
- настроить https