from django.shortcuts import render, redirect, get_object_or_404
from .forms import CarForm, CarPurchaseForm
from .models import Car
from django.conf import settings
import asyncio
import aiohttp
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse


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


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


class CustomLogoutView(LogoutView):
    pass


def send_email(request):
    if request.path == '/shop':
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.image import MIMEImage
        from email.header import Header
        import base64

        login = 'spiritvoideu@gmail.com'
        password = 'qzdzybrhufpbepop'  # App Password or regular Gmail

        try:
            # Connect to the SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(login, password)

            subject = 'Тема вашего HTML-письма'

            # Указываем путь до файла с HTML-контентом и изображением
            html_file_path = '/home/lirik12/PycharmProjects/pythonProject7/car-catalog/car_catalog/catalog/templates/send_mail/this.html'
            image_path = '/home/lirik12/PycharmProjects/pythonProject7/car-catalog/car_catalog/media/car_images/mclaren.jpeg'

            # Читаем содержимое HTML-файла
            with open(html_file_path, 'r', encoding='utf-8') as html_file:
                html_content = html_file.read()

            # Создаем MIMEMultipart object
            msg = MIMEMultipart()
            msg['Subject'] = Header(subject, 'utf-8')

            # Читаем содержимое изображения и кодируем в base64
            with open(image_path, 'rb') as image_file:
                image_data = image_file.read()
                image_base64 = base64.b64encode(image_data).decode('utf-8')

            # Attach HTML content with image to the email
            msg.attach(MIMEText(html_content, 'html'))

            # Attach image to the email as inline
            image_attachment = MIMEImage(image_data, name='image.jpg')
            image_attachment.add_header('Content-ID', '<image>')
            msg.attach(image_attachment)

            # Send the email
            server.sendmail(login, 'spiritvoideu@gmail.com', msg.as_string())
            return HttpResponse("Email sent successfully!")

        finally:
            # Ensure the connection is closed
            server.quit()
    else:
        return HttpResponse("Invalid URL")



