from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from waypoints.apis import GoogleMapsAPI, OpenWeatherAPI
from django.core.cache import cache
import json

class AppView(View):
    """
        This class consists of the backend code for the view of the application.
        When the application receives a GET request the get method is called, and depending on the
        content of the request, the request is relayed to one of the other methods.
    """
    template_name = 'addresses.html'

    def get(self, request):
        """
        A method that serves GET requests and offloads the processing to other methods.

        Parameters:
        -----------------------
        arg1 : request
            Django HTTPRequest object received from the web page.

        Returns
        ----------------------
        HTTPResponse
            Django HTTPResponse object that, if it has json data is a JsonResponse.
            Contains either the html for the web page or json data.
        """

        if 'origin' in request.GET:
            return self.get_maps_data(request)
        elif 'lat' in request.GET:
            return self.get_weather_data(request)
        else:
            return render(request, self.template_name, None)

    def get_maps_data(self, request):
        """
        A method used to get json data from the cache, persistent database, or from the
        Google Maps API.

        Parameters:
        -----------------------
        arg1 : request
            Django HTTPRequest object received from the web page.

        Returns
        ----------------------
        JsonResponse
            Carries the json data for the requested route.
        """
        origin = request.GET['origin']
        destination = request.GET['destination']

        key = origin + ' ' + destination

        directions = cache.get_or_set(key, GoogleMapsAPI.get_directions(origin, destination))

        return JsonResponse(directions, safe=False)

    def get_weather_data(self, request):
        """
        A method used to get json data from the cache, persistent database, or from the
        OpenWeather API.

        Parameters:
        -----------------------------------------------------------------------------
        arg1 : request
            Django HTTPRequest object received from the web page.

        Returns
        -----------------------------------------------------------------------------
        JsonResponse
            Carries the json data for the requested geo coordinate from the map.
        """

        lat = request.GET['lat']
        lng = request.GET['lng']

        key = str(lat) + ' ' + str(lng)

        weather = cache.get_or_set(key, OpenWeatherAPI.get_weather(lat, lng), None)

        return JsonResponse(weather, safe=False)