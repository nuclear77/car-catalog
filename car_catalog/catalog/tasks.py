from celery import Celery
from celery.schedules import crontab
import requests
from celery import shared_task
from .models import CurrencyPrice
from decimal import Decimal
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


@shared_task
def fetch_binance_price():
    try:
        response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'bnbusdt'})
        response.raise_for_status()  # Проверка наличия ошибок HTTP
        data = response.json()
        price = Decimal(data.get('price'))

        CurrencyPrice.objects.create(symbol='bnbusdt', price=price)

        print(f'Binance BNBUSDT Price: {price}')

    except Exception as e:
        print(f'Error fetching Binance price: {e}')


app = Celery('myapp')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Запуск задачи каждые 45 секунд
app.conf.beat_schedule = {
    'fetch_binance_price': {
        'task': 'myapp.tasks.fetch_binance_price',
        'schedule': 45.0,
    },
}