from django.db import models
from PIL import Image


class CarAPI(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='car_images', default='default_image.jpg')

    class Meta:
        app_label = 'catalog'

    def __str__(self):
        return f"{self.make} {self.model}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)
            img.save(self.image.path)


class Message(models.Model):
    sender = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.content}'