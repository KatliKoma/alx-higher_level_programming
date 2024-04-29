#!/usr/bin/python3

"""
This script fetches the 'X-Request-Id' header value from a URL provided as a command-line argument using urllib.request.
"""

import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        value = html.get('X-Request-Id')
        print(value)
