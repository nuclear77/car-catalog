# Generated by Django 4.2.7 on 2023-12-10 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_remove_carapi_link'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CarAPI',
        ),
    ]
