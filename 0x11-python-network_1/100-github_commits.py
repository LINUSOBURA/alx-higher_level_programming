#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”
"""
from sys import argv

import requests

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    resp_jsn = response.json()

    for item in resp_jsn[:10]:
        sha = item['sha']
        commit = item['commit']
        author = commit['author']
        name = author['name']
        print(f"{sha}: {name}")
