import requests

def get_weather(latitude, longitude):

        url = "https://api.open-meteo.com/v1/forecast"

        params ={                                    
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True
        }

        response = requests.get(url, params=params)

        data = response.json()

        temperature = data["current_weather"]["temperature"]

        symbol = data["current_weather_units"]["temperature"]

        result = f"{temperature} {symbol}"

        return result