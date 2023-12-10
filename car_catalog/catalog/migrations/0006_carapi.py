# Generated by Django 4.2.7 on 2023-12-10 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_car_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarAPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('image', models.ImageField(default='default_image.jpg', upload_to='car_images')),
                ('link', models.URLField()),
            ],
        ),
    ]
