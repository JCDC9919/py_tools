
from aiohttp import request
import requests
import constants





BASE_URL = "https://api.openweathermap.org/data/2.5/weather"




city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={constants.API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(f"weather is {weather}.")
    temp = round(data['main']['temp'] - 273.15,2)
    print(f"temperature in Celsius is {temp}.")
    

else:
    print("Error, please check correct city entered")
