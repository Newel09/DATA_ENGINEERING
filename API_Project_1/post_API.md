import requests
import csv

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url)

print(response.status_code)

if response.status_code == 200:
    data = response.json()
    with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['userId', 'id', 'title', 'body']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for post in data:
            writer.writerow({
                "userId": post['userId'],
                "id": post['id'],
                "title": post['title'],
                "body": post['body']
            })

    print("posts.csv file has been created successfully.")
            
else:
    print("Failed to retrieve data.")