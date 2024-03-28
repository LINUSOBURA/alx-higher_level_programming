#!/usr/bin/python3
"""
Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys

import requests

if len(sys.argv) == 1:
    letter = ""
else:
    letter = sys.argv[1]

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, params={"q": letter})
    try:
        json_resp = response.json()
        if json_resp:
            for item in json_resp:
                print("[{}] {}".format(item['id'], item['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
