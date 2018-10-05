import models
from apis import GoogleMapsAPI

tests = [{'origin': 'Buffalo, NY', 'destination':'Albany, NY'}, {'origin': 'Buffalo, NY', 'destination':'Rochester, NY'}, {'origin': 'Buffalo, NY', 'destination':'Erie, NY'}]

for test in tests:
    directions = GoogleMapsAPI.get_directions(test['origin'], test['destination'])
    model = models.MapsDataModel(origin=test['origin'], destination=test['destination'], data=directions)
    model.save()

print(models.MapsDataModel.objects.all())