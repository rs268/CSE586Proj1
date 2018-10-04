import googlemaps
from datetime import datetime

class GoogleMapsAPI:

    @staticmethod
    def get_directions(from_address, to_address):
        now = datetime.now()
        gmaps = googlemaps.Client(key='AIzaSyC4LCIevV75PkJtJaPDi1rbqIkImDgo2S0')

        return gmaps.directions(from_address, to_address, mode='driving', departure_time=now)

class OpenWeatherAPI:

    @staticmethod
    def get_weather(lat, lng):
        pass