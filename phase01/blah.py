import json

with open('blah.json', 'r') as i:
    r = json.load(i)

    for step in r[0]['legs'][0]['steps']:
        for key in step:
            if key == 'start_location' or key == 'end_location':
                step[key]['lat'] = str(step[key]['lat'])
                step[key]['lng'] = str(step[key]['lng'])

    with open('blah_fix.json', 'w') as f:
        json.dump(r, f)