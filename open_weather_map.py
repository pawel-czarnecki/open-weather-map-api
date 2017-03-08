from urllib.request import urlopen
import json


class OpenWeatherMap:
    def __init__(self, api_key):
        self.current_weather_url = "http://api.openweathermap.org/data/2.5/weather"
        self.api_key = api_key

    @staticmethod
    def parse_json(self, api_url):
        request = urlopen(api_url).read().decode('UTF-8')
        return json.loads(request)
