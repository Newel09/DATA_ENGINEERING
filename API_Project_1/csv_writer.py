import requests
import csv

def save_to_csv(data):
    with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['userId', 'id', 'title', 'body']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for post in data:
            writer.writerow({
                "userId": post["userId"],
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })