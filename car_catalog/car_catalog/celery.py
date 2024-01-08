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


app = Celery('catalog')
app.config_from_object('django.conf:settings', namespace='CELERY')

app = Celery('car_catalog')

app.conf.beat_schedule = {
    'fetch-binance-price': {
        'task': 'catalog.tasks.fetch_binance_price',
        'schedule': timedelta(seconds=20),
    },
}