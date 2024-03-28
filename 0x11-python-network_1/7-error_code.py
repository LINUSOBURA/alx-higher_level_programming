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
        response.raise_for_status()
    except requests.HTTPError as error:
        print("Error code: {}".format(error))
