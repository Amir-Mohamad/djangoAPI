import requests
import json


def get_data(username):
    # user account
    url = f"https://api.github.com/users/{username}"
    # getting user account data from github api
    r = requests.get(url)
    # json
    data_json = r.json()    
    return data_json