from django.db import models

# Create your models here.
class MapsDataModel(models.Model):
    """
    This class represents the rows of the table in the
    database that holds the Google Maps API data.

    Parameters:
    --------------------------------------------
    origin : string
        The origin entered by the user.
    destination : string
        The destination entered by the user.
    data : string
        The json data from the Google Maps API
    objects : Django Manager
        Used for querying the database
    """

    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    data = models.TextField()

    objects = models.Manager()


class WeatherDataModel(models.Model):
    """
    This class represents the rows of the table in the
    database that holds the Google Maps API data.

    Parameters:
    ----------------------------------------------------
    lat : string
        The lat of the marker that was clicked on.
    lng : string
        The lng of the marker that was clicked on.
    data : string
        The json data from the OpenWeather API.
    objects : Django Manager
        Used for querying the database.
    """

    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    data = models.TextField()

    objects = models.Manager()