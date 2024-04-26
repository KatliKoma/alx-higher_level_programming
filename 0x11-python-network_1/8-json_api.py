#!/usr/bin/python3

"""
This script takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
If no argument is given, it sets q="".
If the response body is properly JSON formatted and not empty, it displays the id and name.
Otherwise, it displays appropriate error messages.
"""

import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    
    try:
        response = requests.post(url, data={'q': q})
        data = response.json()

        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
