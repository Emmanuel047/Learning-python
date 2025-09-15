#practising my api skills in python
#my endpoint is "https://jsonplaceholder.typicode.com"/

import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
users = response.json()
email = [user['email'] for user in users]
names = [user['name'] for user in users]
for user in users:
    print(f"Name: {user['name']},  Email: {user['email']}")