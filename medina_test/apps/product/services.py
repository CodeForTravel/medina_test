import requests
from django.conf import settings
from constance import config as constance_config


class WeatherService:
    def __init__(self):
        self.weather_api_url = settings.WEATHER_API_URL
        self.api_key = settings.WEATHER_API_KEY
        self.latitude = settings.LATITUDE
        self.longitude = settings.LONGITUDE

    def fetch_weather_data(self):
        weather_url = f"{self.weather_api_url}?lat={self.latitude}&lon={self.longitude}&units=metric&appid={self.api_key}"
        response = requests.get(weather_url)

        if response.status_code == 200:
            json_response = response.json()
            weather_main = json_response.get("weather")[0].get("main")
            temp = json_response.get("main").get("temp")
            temp_min = json_response.get("main").get("temp_min")
            temp_max = json_response.get("main").get("temp_max")
            new_weather_data = {
                "main": weather_main,
                "temp": temp,
                "temp_min": temp_min,
                "temp_max": temp_max, 
            }
            constance_config.WEATHER_DATA = str(new_weather_data)
