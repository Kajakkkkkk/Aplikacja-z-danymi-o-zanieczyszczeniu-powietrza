import requests
import os
from translate import translate_data


class AirVisualAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.airvisual.com/v2"

    def get_city_data(self, city, state, country):
        url = f"{self.base_url}/city?city={city}&state={state}&country={country}&key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        translated_data = translate_data(data)
        print(translated_data)


API_KEY = os.getenv('AIR_VISUAL_API_KEY', '3beb55b3-c389-4e04-b69f-7e6f1879ed84')
client = AirVisualAPI(API_KEY)
client.get_city_data('Warsaw', 'Mazovia', 'Poland')
