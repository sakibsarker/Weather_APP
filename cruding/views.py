from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request
# Create your views here.

def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        API_KEY = 'b9a819e1db03f2a8e0f68f5303e8e1e2'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
        
        # Make the API request
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())

        # Extract relevant information from the API response
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']

        # Pass the weather data to the template
        context = {
            'city': city,
            'temperature': temperature,
            'humidity': humidity,
            'weather_description': weather_description
        }
        return render(request, "index.html", context)
    else:
        return render(request, "index.html")

