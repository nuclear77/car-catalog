from celery import Celery
from celery import shared_task
import requests
from datetime import timedelta

@shared_task
def go_binance():
    key = "https://api.binance.com/api/v3/ticker/price?symbol="
    symbol_to_find = "BNBUSDT"

    url = key + symbol_to_find
    response = requests.get(url)
    data = response.json()

    if 'symbol' in data and 'price' in data:
        print(f"{data['symbol']} price is {data['price']}")
    else:
        print(f"Data not found for symbol: {symbol_to_find}")


