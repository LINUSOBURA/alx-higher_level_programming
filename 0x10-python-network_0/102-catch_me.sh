#!/bin/bash
#Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response #curl -o /dev/null -sw "You got me!"  0.0.0.0:5000/catch_me
curl -sL -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me