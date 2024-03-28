#!/usr/bin/python3
"""
Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys

import requests

if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={"q": letter})
    try:
        json_resp = response.json()
        if json_resp:
            print("[{}] {}".format(json_resp['id'], json_resp['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
