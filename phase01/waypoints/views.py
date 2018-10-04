from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from waypoints.apis import GoogleMapsAPI
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
        #directions = GoogleMapsAPI.get_directions(request.POST['from_address'], request.POST['to_address'])

        with open('blah.json', 'r') as i:
            directions = json.load(i)

        return JsonResponse(directions, safe=False)

    def get_weather_data(self, request):
        return JsonResponse({})