from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from waypoints.apis import GoogleMapsAPI, OpenWeatherAPI
import json

class AppView(View):
    template_name = 'addresses.html'

    def get(self, request):
        if 'from_address' in request.GET:
            return self.get_maps_data(request)
        elif 'lat' in request.GET:
            return self.get_weather_data(request)
        else:
            return render(request, self.template_name, None)

    def get_maps_data(self, request):
        #Check for cached response
        #directions = GoogleMapsAPI.get_directions(request.GET['from_address'], request.GET['to_address'])

        with open('blah.json', 'r') as i:
            directions = json.load(i)

        return JsonResponse(directions, safe=False)

    def get_weather_data(self, request):
        #weather = OpenWeatherAPI.get_weather(request.GET['lat'], request.GET['lng'])

        weather = {"coord":{"lon":139,"lat":35},
                    "sys":{"country":"JP","sunrise":1369769524,"sunset":1369821049},
                    "weather":[{"id":804,"main":"clouds","description":"overcast clouds","icon":"04n"}],
                    "main":{"temp":289.5,"humidity":89,"pressure":1013,"temp_min":287.04,"temp_max":292.04},
                    "wind":{"speed":7.31,"deg":187.002},
                    "rain":{"3h":0},
                    "clouds":{"all":92},
                    "dt":1369824698,
                    "id":1851632,
                    "name":"Shuzenji",
                    "cod":200}

        return JsonResponse(weather, safe=False)