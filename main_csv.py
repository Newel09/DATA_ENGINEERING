
from API_Project_1.API_cli import get_posts
from API_Project_1.csv_writer import save_to_csv

posts = get_posts()

if posts is not None:
    save_to_csv(posts)
    print("Posts saved successfully to posts.csv")