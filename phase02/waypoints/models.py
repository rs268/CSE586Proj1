from django.db import models

# Create your models here.
class MapsDataModel(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    data = models.TextField()


class WeatherDataModel(models.Model):
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    data = models.TextField()
