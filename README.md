# DjangoFileAPI

## Функционал:

- загрузка, хранение, просмотр сохраненных файлов посредством API
- асинхронная обработка файлов с использованием celery

Проект "боевой" (готов к деплою) требуется:
- клонировать проект:
```sh
git clone https://github.com/demetrzz/djangofileapi
```
- создать файл .env в корне проекта по примеру:
```sh
POSTGRES_DB=db
POSTGRES_NAME=djangofileapi
POSTGRES_USER=postgres
POSTGRES_PASSWORD=testpassword
```
- добавить домен/ip сервера в ALLOWED_HOSTS в settings.py:
```sh
ALLOWED_HOSTS = ['YOUR_DOMAIN_HERE']
```
- настроить и запустить контейнеры docker:
```sh
docker compose build
docker compose up
```
- создать базу данных в контейнере:
```sh
docker exec -it container_id psql -U my_user -d my_db --password
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
- вынести ALLOWED_HOSTS в .env файл
- настроить https