#!/usr/bin/python3
"""
ython script that takes in a URL, sends a request
to the URL and displays the body of the response
"""
import sys

import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    try:
        print(response.text)
    except requests.HTTPError:
        print("Error code: {}".format(response.status_code))
