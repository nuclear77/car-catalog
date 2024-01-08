from celery import shared_task
from decimal import Decimal
import requests
from .models import CurrencyPrice


@shared_task
def fetch_binance_price():
    response = requests.get('https://api.binance.com/api/v3/ticker/price')
    data_list = response.json()

    print('API Response:', data_list)

    bnbusdt_data = next((data for data in data_list if data['symbol'] == 'BNBUSDT'), None)

    if bnbusdt_data:
        price = Decimal(bnbusdt_data.get('price'))

        existing_currency = CurrencyPrice.objects.filter(symbol='bnbusdt').first()

        if existing_currency:
            existing_currency.price = price
            existing_currency.save()
        else:
            CurrencyPrice.objects.create(symbol='bnbusdt', price=price)

        print(f'Binance BNBUSDT Price: {price}')
    else:
        print('BNBUSDT data not found in the API response')


