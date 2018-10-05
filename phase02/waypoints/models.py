from django.db import models

# Create your models here.
class MapsDataModel(models.Model):
    origin = models.CharField()
    destination = models.CharField()
    

class WeatherDataModel(models.Model):
    pass
