import requests
import json

def get_data():
    url = f"https://api.github.com/users/Amir-Mohamad"
    r = requests.get(url)
    data_json = r.json()    
    return data_json