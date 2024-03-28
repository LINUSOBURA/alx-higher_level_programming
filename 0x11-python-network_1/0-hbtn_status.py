#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    body = response.read()
    body_type = type(body)
    decoded_body = body.decode("utf-8")

print(
    """Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}""".
    format(body_type, body, decoded_body))
