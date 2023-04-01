#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response
curl -s 0.0.0.0:5000/catch_me -X PUT -L -d "user_id=98" -H "Origin: HolbertonSchool"
