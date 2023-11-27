from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('make', 'model', 'image', 'link')


class CarPurchaseForm(forms.Form):
    make = forms.CharField(label='Марка')
    model = forms.CharField(label='Модель')
    extras = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple,
        label='Дополнения'
    )

    def __init__(self, *args, **kwargs):
        extras_choices = kwargs.pop('extras_choices')
        super().__init__(*args, **kwargs)
        self.fields['extras'].queryset = extras_choices


class ExtrasForm(forms.Form):
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
