#!/usr/bin/python3
# Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
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
