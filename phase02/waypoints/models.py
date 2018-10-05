from django.db import models

# Create your models here.
class MapsDataModel(models.Model):
    origin = models.CharField()
    destination = models.CharField()
    data = models.TextField()


class WeatherDataModel(models.Model):
    lat = models.CharField()
    lng = models.CharField()
    data = models.TextField()
