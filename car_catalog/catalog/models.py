from django.db import models
from PIL import Image


class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    image = models.ImageField(upload_to='car_images')
    link = models.URLField()

    class Meta:
        app_label = 'catalog'

    def __str__(self):
        return f"{self.make} {self.model}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)
            img.save(self.image.path)