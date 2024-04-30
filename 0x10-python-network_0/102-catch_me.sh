#!/bin/bash
# Retrieves and displays the response body from a curl POST request, specifying user_id=98 and Origin header as "HolbertonSchool"
curl -sLX PUT -d "user_id=98" -H "Origin:HolbertonSchool" 0.0.0.0:5000/catch_me
