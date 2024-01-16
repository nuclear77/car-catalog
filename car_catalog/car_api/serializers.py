from rest_framework import serializers
from .models import CarAPI
from .models import Message


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAPI
        fields = ('id', 'make', 'model', 'price', 'image')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['sender', 'content', 'timestamp']
