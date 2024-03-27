#!/bin/bash
# Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -sL "$1" -X GET -H "X-School-User-Id:98"
