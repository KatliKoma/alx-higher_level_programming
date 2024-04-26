#!/usr/bin/python3

"""
This script sends a POST request to a URL with an email parameter.
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url, email = sys.argv[1], sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('ascii')

    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))

