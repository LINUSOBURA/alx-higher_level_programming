#!/usr/bin/python3
# Python script that dusplays a particular header
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_id = response.getheader("X-Request-Id")
    print(x_id)
