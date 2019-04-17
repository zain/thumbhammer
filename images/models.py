from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Image(models.Model):
    name = models.CharField(max_length=255)
    original = models.ImageField(upload_to="media")
    thumbnail = ImageSpecField(source="original", processors=[ResizeToFill(300, 300)])

    def __str__(self):
        return self.name
