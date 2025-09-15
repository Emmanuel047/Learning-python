import requests
import re
#Validate url input
def validate_url():
    while True:
        url = input("Enter your api link: ")
        if url == "":
            print("No link provided")
            continue
        elif not re.search('^(https?://)', url):
            print("Link must start with http:// or https://")
            continue
        else:
            break
    return url
url = validate_url()   
def fetch_status(validate_url):
    try:
        response = requests.get(validate_url, timeout = 5)
        if response.status_code != 200:
            return f"Error the status code of the api link is {response.status_code}"
        return f"Success the response is {response.status_code} "
    except requests.exceptions.Timeout:
        return "Request timeout."
    except requests.exceptions.ConnectionError:
        return "Error the api link is broken"
print(fetch_status(url))