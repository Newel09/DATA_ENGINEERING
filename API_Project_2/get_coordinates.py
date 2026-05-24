import requests

def get_coordinates(city):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name":city,
        "count":1,
        "language":"en",
        "format":"json"
    }

    response = requests.get(url, params=params)

    data = response.json()

    location = data['results'][0]

    result = {
        "city": location["name"], 
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "country": location["country"]
    }

    return result