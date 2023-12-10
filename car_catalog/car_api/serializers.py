from rest_framework import serializers
from .models import CarAPI


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAPI
        fields = ('id', 'make', 'model', 'price', 'image')
