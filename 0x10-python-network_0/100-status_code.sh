#!/bin/bash
# Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response
curl -s "$1" -w "%{http_code}" -o /dev/null
