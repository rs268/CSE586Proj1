from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from waypoints.apis import GoogleMapsAPI, OpenWeatherAPI
from django.core.cache import cache
import json

class AppView(View):
    template_name = 'addresses.html'

    def get(self, request):
        if 'origin' in request.GET:
            return self.get_maps_data(request)
        elif 'lat' in request.GET:
            return self.get_weather_data(request)
        else:
            return render(request, self.template_name, None)

    def get_maps_data(self, request):
        origin = request.GET['origin']
        destination = request.GET['destination']

        key = origin + ' ' + destination

        directions = cache.get_or_set(key, GoogleMapsAPI.get_directions(origin, destination))

        return JsonResponse(directions, safe=False)

    def get_weather_data(self, request):

        lat = request.GET['lat']
        lng = request.GET['lng']

        key = str(lat) + ' ' + str(lng)

        weather = cache.get_or_set(key, OpenWeatherAPI.get_weather(lat, lng), None)

        return JsonResponse(weather, safe=False)