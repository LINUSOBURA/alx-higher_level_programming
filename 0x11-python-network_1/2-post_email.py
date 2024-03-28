#!/usr/bin/python3
# sends post request and returns a response
import urllib.parse
import urllib.request
from sys import argv

url = argv[1]
values = {'email': argv[2]}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
reqs = urllib.request.Request(url, data)

with urllib.request.urlopen(reqs) as response:
    body = response.read()
    decoded_body = body.decode('utf-8')

print(decoded_body)
