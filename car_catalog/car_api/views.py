from rest_framework import status
from rest_framework.decorators import api_view
from .models import Car
from .serializers import CarSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(['GET'])
def car_list(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def car_search(request):
    q = request.GET.get('q')
    cars = Car.objects.filter(make__icontains=q) | Car.objects.filter(model__icontains=q)
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def car_create(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def car_update(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CarSerializer(car, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def car_delete(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    car.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
