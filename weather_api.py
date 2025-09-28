import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://weather.googleapis.com/v1/forecast/hours:lookup"
API_KEY = os.getenv('GOOGLE_WEATHER_API_KEY')


def get_weather_data(latitude, longitude):
    params = {
        "location.latitude": latitude,
        "location.longitude": longitude,
        "hours": 10,
        "key": API_KEY
    }
    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    return response.json()
