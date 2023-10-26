import requests
import json
from django.shortcuts import render


def display_temp(request):

    response = requests.get('https://io.adafruit.com/api/v2/Naura_iot/feeds/temperature')

    print(response.status_code)

    json_clean = json.dumps(response.json(), indent=4)
    json_clean = json.loads(json_clean)

    response = json_clean.get('last_value')
    return render(request, 'home.html', {'response': response})


