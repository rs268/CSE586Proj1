import googlemaps
from datetime import datetime
import requests

class GoogleMapsAPI:

    @staticmethod
    def get_directions(from_address, to_address):
        now = datetime.now()
        gmaps = googlemaps.Client(key='AIzaSyC4LCIevV75PkJtJaPDi1rbqIkImDgo2S0')

        return gmaps.directions(from_address, to_address, mode='driving', departure_time=now)

class OpenWeatherAPI:

    @staticmethod
    def get_weather(lat, lng):
        url = 'http://api.openweathermap.org/data/2.5/weather?'
        url += 'lat=' + str(lat)
        url += '&lon=' + str(lng)
        url += '&APPID=31bc1029c088bbd3d37ee24dd5bfd134'

        response = requests.get(url)

        return response.json()