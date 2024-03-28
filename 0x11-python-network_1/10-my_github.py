#!/usr/bin/python3
"""
ython script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import sys

import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    usrname = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(url, auth=(usrname, password))

    if response.status_code == 200:
        user_data = response.json()
        print(user_data['id'])
    else:
        print(None)
