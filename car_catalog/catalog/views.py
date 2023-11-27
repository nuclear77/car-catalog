from django.shortcuts import render, redirect, get_object_or_404
from .forms import CarForm, CarPurchaseForm
from .models import Car, Extras


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


def purchase_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        form = CarPurchaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('purchase_success')
    else:
        form = CarPurchaseForm(extras_choices=Car.objects.all())

    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'purchase_car.html', context)


def select_extras(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == 'POST':
        selected_extras = request.POST.getlist('extras')
        return redirect('purchase_car')
    else:
        return render(request, 'select_extras.html', {'car': car})