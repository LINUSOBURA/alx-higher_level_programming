#!/usr/bin/python3
"""
 Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    body = response.text
    b_type = type(body)
    print("""Body response:\n\t- type: {}\n\t- content: {}""".format(
        b_type, body))
