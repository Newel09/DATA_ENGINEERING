import requests
import csv

url = 'https://jsonplaceholder.typicode.com/posts'

def get_posts():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve data.")
        print("Status Code:", response.status_code)
        return None