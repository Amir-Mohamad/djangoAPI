import requests
import json

def get_data():
    url = f"https://api.github.com/users/Amir-Mohamad"
    r = requests.get(url)
    data = r.json()
    data_list = [i for i in data['id']]
    return data_list
