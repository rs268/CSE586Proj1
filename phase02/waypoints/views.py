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

        # weather = {"coord":{"lon":139,"lat":35},
        #             "sys":{"country":"JP","sunrise":1369769524,"sunset":1369821049},
        #             "weather":[{"id":804,"main":"clouds","description":"overcast clouds","icon":"04n"}],
        #             "main":{"temp":289.5,"humidity":89,"pressure":1013,"temp_min":287.04,"temp_max":292.04},
        #             "wind":{"speed":7.31,"deg":187.002},
        #             "rain":{"3h":0},
        #             "clouds":{"all":92},
        #             "dt":1369824698,
        #             "id":1851632,
        #             "name":"Shuzenji",
        #             "cod":200}

        return JsonResponse(weather, safe=False)