# Generated by Django 4.2.7 on 2023-12-10 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_carapi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carapi',
            name='link',
        ),
    ]
