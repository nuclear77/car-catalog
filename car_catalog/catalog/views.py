from django.shortcuts import render
from .models import Car


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})


def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'car_detail.html', {'car': car})


def car_catalog(request):
    cars = Car.objects.all()
    return render(request, 'car_catalog.html', {'cars': cars})