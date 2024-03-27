#!/usr/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -I "$1" | grep -Fi "Content-Length" | awk -F ': ' '{print $2}'
