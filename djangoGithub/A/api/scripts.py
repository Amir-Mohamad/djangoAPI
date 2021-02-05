import requests
import json

def get_data():
    url = f"https://api.github.com/users/Amir-Mohamad"
    r = requests.get(url)
    data = r.json()
    for key, value in data.items():
        return(key, value)
    
