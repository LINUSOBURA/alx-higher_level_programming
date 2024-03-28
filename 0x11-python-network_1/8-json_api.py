#!/usr/bin/python3
"""
Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys

import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, params={"q": sys.argv[1]})
    json_resp = response.json()
    if json_resp:
        for item in json_resp["items"]:
            print("[{}] {}".format({item['id'], item['name']}))
    elif json_resp == {}:
        print("No result")
    else:
        print("Not a valid JSON")
    print(json_resp)
