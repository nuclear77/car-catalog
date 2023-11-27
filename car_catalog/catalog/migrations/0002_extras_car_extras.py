# Generated by Django 4.2.7 on 2023-11-27 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='extras',
            field=models.ManyToManyField(to='catalog.extras'),
        ),
    ]
