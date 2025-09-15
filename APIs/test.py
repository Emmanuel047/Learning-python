import requests
response = requests.get("https://api.thecatapi.com/v1/breeds/abys")

print(response.headers.get("Content-type"))
print(response.json()["description"])
print(response.headers)