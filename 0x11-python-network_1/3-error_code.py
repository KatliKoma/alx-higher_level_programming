#!/usr/bin/python3

"""
This script sends a request to a URL and displays the response body. 
If an HTTP error occurs, it prints the error code.
"""

import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    parameter = urllib.parse.urlencode(value).encode('ascii')

    request = urllib.request.Request(url, parameter)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
