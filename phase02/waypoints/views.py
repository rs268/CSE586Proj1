from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from waypoints.apis import GoogleMapsAPI, OpenWeatherAPI
from django.core.cache import cache
from waypoints.models import MapsDataModel, WeatherDataModel
from django.core.exceptions import ObjectDoesNotExist
import sys, warnings
import json

if not sys.warnoptions:
    warnings.simplefilter('ignore')

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

        c = cache.get(key)

        if c:
            directions = json.loads(c)
        else:
            try:
                query = MapsDataModel.objects.get(origin=origin, destination=destination)
                directions = json.loads(query.data)
                cache.set(key, json.dumps(directions))

            except ObjectDoesNotExist:
                directions = GoogleMapsAPI.get_directions(origin, destination)
                cache.set(key, json.dumps(directions))
                model = MapsDataModel(origin=origin, destination=destination, data=json.dumps(directions))
                model.save()

        return JsonResponse(directions, safe=False)

    def get_weather_data(self, request):

        lat = request.GET['lat']
        lng = request.GET['lng']

        key = str(lat) + ' ' + str(lng)

        c = cache.get(key)

        if c:
            weather = json.loads(c)
        else:
            try:
                query = WeatherDataModel.objects.get(lat=str(lat), lng=str(lng))
                weather = json.loads(query.data)
                cache.set(key, json.dumps(weather))

            except ObjectDoesNotExist:
                weather = OpenWeatherAPI.get_weather(lat, lng)
                cache.set(key, json.dumps(weather))
                model = WeatherDataModel(lat=str(lat), lng=str(lng), data=json.dumps(weather))
                model.save()

        return JsonResponse(weather, safe=False)