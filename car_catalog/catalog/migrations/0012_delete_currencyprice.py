# Generated by Django 4.2.7 on 2024-01-09 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_currencyprice_symbol'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CurrencyPrice',
        ),
    ]
