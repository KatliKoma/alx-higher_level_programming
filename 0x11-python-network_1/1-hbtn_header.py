#!/usr/bin/python3
import urllib.request
import sys
"""
This script fetches the 'X-Request-Id' header value from a URL provided as a command-line argument using urllib.request.
"""

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
