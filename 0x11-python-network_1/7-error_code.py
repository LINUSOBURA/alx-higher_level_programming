#!/usr/bin/python3
"""
ython script that takes in a URL, sends a request
to the URL and displays the body of the response
"""
import sys

import requests.exceptions

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text)
        else:
            response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Error code: {}".format(response.status_code))
