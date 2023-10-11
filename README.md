# DjangoFileAPI

## Функционал:

- загрузка, хранение, просмотр сохраненных файлов посредством API
- асинхронная обработка файлов с использованием celery
- проект "боевой" (готов к деплою), требуется создать файл .env в корне проекта по примеру:
```sh
POSTGRES_DB=db
POSTGRES_NAME=djangofileapi
POSTGRES_USER=postgres
POSTGRES_PASSWORD=testpassword
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
