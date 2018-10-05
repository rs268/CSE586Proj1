import googlemaps
from datetime import datetime
import requests

class GoogleMapsAPI:
    """
    A class that acts as an interface to the Google Maps Python Client.
    """

    @staticmethod
    def get_directions(origin, destination):
        """
        A static method called by the view to get the routes between origin and destination.

        Parameters:
        ---------------------------------------------------------------------
        origin : string
            The origin of the route entered by the user.
        destination : string
            The destination of the route entered by the user.

        Returns:
        ---------------------------------------------------------------------
        list
            Json of directions from origin to destination.
        """
        now = datetime.now()
        gmaps = googlemaps.Client(key='YOUR_API_KEY_HERE')

        return gmaps.directions(origin, destination, mode='driving', departure_time=now)

class OpenWeatherAPI:
    """
    A class that acts as an interface to the OpenWeather API.
    """

    @staticmethod
    def get_weather(lat, lng):
        """
        A static method called by the view to get the weather at a latitude and longitude.

        Parameters:
        ---------------------------------------------------------------------
        lat : string
            The latitude of the marker that was clicked.
        lng : string
            The longitude of the marker that was clicked.

        Returns:
        ---------------------------------------------------------------------
        list
            Json of weather data.
        """

        url = 'http://api.openweathermap.org/data/2.5/weather?'
        url += 'lat=' + str(lat)
        url += '&lon=' + str(lng)
        url += '&APPID=YOUR_API_KEY_HERE'

        response = requests.get(url)

        return response.json()