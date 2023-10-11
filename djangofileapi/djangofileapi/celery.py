import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangofileapi.settings')

app = Celery('djangofileapi')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
