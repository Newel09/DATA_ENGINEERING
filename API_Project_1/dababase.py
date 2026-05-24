import sqlite3

dp_path = r'C:/Users/user/ALX-C10_DATA_SCIENCE/Data_Engineering/api_project.db'
conn = sqlite3.connect(dp_path)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INT PRIMARY KEY, id INT, title VARCHAR(255), body TEXT)")
conn.commit()



