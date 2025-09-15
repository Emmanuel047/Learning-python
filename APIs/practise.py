#practising my api skills in python
#my endpoint is https://jsonplaceholder.typicode.com/

import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
users = response.json()
email = users
names = [users['name'] for users in users]
print(names[0])