from rest_framework import status
from rest_framework.decorators import api_view
from .models import Car
from .serializers import CarSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# @api_view(['GET'])
# def car_search(request):
#     q = request.GET.get('q')
#     cars = Car.objects.filter(make__icontains=q) | Car.objects.filter(model__icontains=q)
#     serializer = CarSerializer(cars, many=True)
#     return Response(serializer.data)


#начало новых классов из дз
class PurchaseList(generics.ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        name_1 = self.kwargs['make']
        return Car.objects.filter(make=name_1)


class CarCreateAPIView(CreateAPIView):
    serializer_class = CarSerializer


class CarListAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    # filter_backends = [DjangoFilterBackend]
    # filter_backends = [filters.SearchFilter]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['make', 'model']
    # filterset_fields = ['price']
    # search_fields = ['make', 'model']


class CarRetrieveAPIView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'pk'


class CarDestroyAPIView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'pk'


class CarUpdateAPIView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'pk'


class CarListCreateAPIView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'pk'


class CarRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'pk'