from django.shortcuts import render, redirect, get_object_or_404
from .forms import CarForm, CarPurchaseForm
from .models import Car
from django.conf import settings
import asyncio
import aiohttp
import datetime


def car_list(request):
    cars = Car.objects.all()

    return render(request, 'car_list.html', {'cars': cars})


def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'car_detail.html', {'car': car})


def car_catalog(request):
    cars = Car.objects.all()
    return render(request, 'car_catalog.html', {'cars': cars})


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()

    return render(request, 'add_car.html', {'form': form})


def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)

    return render(request, 'edit_car.html', {'form': form, 'car': car})


def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')

    return render(request, 'delete_car.html', {'car': car})


async def send_telegram_notification(bot_token, chat_id, message):
    async with aiohttp.ClientSession() as session:
        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        payload = {
            'chat_id': chat_id,
            'text': message
        }
        async with session.post(url, data=payload) as response:
            response_data = await response.json()
            if not response_data['ok']:
                print('Ошибка при отправке уведомления в Telegram:', response_data['description'])


def purchase_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        form = CarPurchaseForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            extras = form.cleaned_data['extras']

            delivery_date = datetime.date.today() + datetime.timedelta(days=3)

            # Отправка уведомления в Telegram
            bot_token = settings.TELEGRAM_BOT_TOKEN
            chat_id = settings.TELEGRAM_CHAT_ID
            message = f"Машина '{car.make} {car.model}' была куплена заказчиком '{name}'. " \
                      f"Дата доставки: {delivery_date.strftime('%Y-%m-%d')}."

            asyncio.run(send_telegram_notification(bot_token, chat_id, message))

            return redirect('/')
    else:
        form = CarPurchaseForm()
        extras_choices = [(extra, extra) for extra in car.extras.all().values_list('name', flat=True)]

    extras_form = CarPurchaseForm()

    context = {
        'form': CarPurchaseForm,
        'car': car,
        'extras_form': extras_form,
    }
    return render(request, 'purchase_car.html', context)


