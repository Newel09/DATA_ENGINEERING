from .get_coordinates import get_coordinates
from .get_weather import get_weather

def get_city_temperature(city):
    location = get_coordinates(city)

    latitude = location["latitude"]

    longitude = location["longitude"]

    temperature = get_weather(latitude, longitude)

    return temperature