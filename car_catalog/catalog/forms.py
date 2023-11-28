from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('make', 'model', 'price', 'image', 'link')


class CarPurchaseForm(forms.Form):
    name = forms.CharField(label='Имя заказчика')
    CHOICES = (
        ('floor_mats', 'Коврики'),
        ('rain_guard', 'Антидождь'),
        ('parking_sensors', 'Парктроники'),
    )
    extras = forms.MultipleChoiceField(
        choices=CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='Дополнения'
    )


