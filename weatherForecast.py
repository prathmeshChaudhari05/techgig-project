# wether forecast using OpenWeatherMap API
import requests
import json

api_key = 'ad2706636ddfcf6579b8e07d682d9e68'

#make a function to accept city name and return weather forecast
def weatherForecast(city_name):
    try:
        base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
        resp = requests.get(base_url).json()
        return resp['main']['temp']
    except KeyError:
        return 'City not found'

city = input("Enter the city name: ")
if weatherForecast(city) == 'City not found':
    print("City not found")
else:
    print(f"Today's Current Weather of {city} is {weatherForecast(city)} degree celcius")
