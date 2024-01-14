from __future__ import absolute_import, unicode_literals
from celery.schedules import timedelta
import os
from celery import Celery
from django.conf import settings

import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_catalog.settings')

app = Celery('car_catalog')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'go-binance-task': {
        'task': 'catalog.tasks.go_binance',
        'schedule': timedelta(seconds=40),
    },
}