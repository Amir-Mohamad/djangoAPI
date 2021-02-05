import requests
import json

def get_data(username):
    url = f"https://api.github.com/users/{username}"
    r = requests.get(url)
    data_json = r.json()    
    return data_json