from rest_framework import status
from rest_framework.decorators import api_view
from .models import CarAPI
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
from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.drawing.image import Image as ExcelImage
from PIL import Image as PILImage
from io import BytesIO
from .models import Message
from .serializers import MessageSerializer




class PurchaseList(generics.ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        name_1 = self.kwargs['make']
        return CarAPI.objects.filter(make=name_1)


class CarCreateAPIView(CreateAPIView):
    serializer_class = CarSerializer


class CarListAPIView(generics.ListAPIView):
    queryset = CarAPI.objects.all()
    serializer_class = CarSerializer
    # filter_backends = [DjangoFilterBackend]
    # filter_backends = [filters.SearchFilter]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['make', 'model']
    # filterset_fields = ['price']
    # search_fields = ['make', 'model']


class CarRetrieveAPIView(RetrieveAPIView):
    queryset = CarAPI.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'pk'


class CarDestroyAPIView(DestroyAPIView):
    queryset = CarAPI.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'pk'


class CarUpdateAPIView(UpdateAPIView):
    queryset = CarAPI.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'pk'


class CarListCreateAPIView(ListCreateAPIView):
    queryset = CarAPI.objects.all()
    serializer_class = CarSerializer


class CarRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = CarAPI.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'pk'


class CarRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = CarAPI.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'pk'


def export_cars_to_excel(request):
    workbook = Workbook()
    sheet = workbook.active

    cars = CarAPI.objects.all()

    sheet.append(['Make', 'Model', 'Price', 'Image'])

    for car in cars:
        try:
            img = PILImage.open(car.image.path)

            img_buffer = BytesIO()

            img.save(img_buffer, format='PNG')

            excel_img = ExcelImage(img_buffer)
            excel_img.width = 60
            excel_img.height = 40

            sheet.append([car.make, car.model, car.price, ''])
            sheet.add_image(excel_img, f'D4')

        except Exception as e:
            print(f"Error processing image for car {car.id}: {str(e)}")

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=cars.xlsx'

    workbook.save(response)

    return response


@api_view(['GET'])
def get_chat_messages(request):
    messages = Message.objects.all()

    # Сериализуем данные для передачи в формат JSON
    serializer = MessageSerializer(messages, many=True)

    return Response(serializer.data)
